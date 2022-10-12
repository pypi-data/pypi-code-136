import os
from datetime import datetime
from urllib.parse import parse_qs, urlparse

import requests
from fyers_api import accessToken, fyersModel
from fyers_api.Websocket import ws

current_directory=os.path.dirname(os.path.realpath(__file__))

data_path=os.path.join(current_directory, "data")
data_file=datetime.now().strftime("%Y-%m-%d")
fyers_access_token_path=os.path.join(data_path, data_file)

log_path=os.path.join(current_directory, "logs")

class FyersApiConfig:
  def __init__(self, config):
    self.username=config['username']
    self.password=config['password']
    self.pin=config['pin']
    self.client_id=config['client_id']
    self.secret_key=config['secret_key']
    self.redirect_uri=config['redirect_uri']

class FyersApiBuilder:
  def __init__(self, config):
    self.config=FyersApiConfig(config)

    self._generate_folders()
    self._init()

  def _generate_folders(self):
    if not os.path.exists(data_path):
      os.makedirs(data_path)

    if not os.path.exists(log_path):
      os.makedirs(log_path)

  def _set_initial_values(self, token):
    self.access_token = token
    self.websocket_access_token = f"{self.config.client_id}:{self.access_token}"
    self.client = fyersModel.FyersModel(client_id=self.config.client_id, token=token, log_path=log_path)
    self.ws_client = ws.FyersSocket(access_token=self.websocket_access_token, run_background=True, log_path=log_path)

  def _init(self):
    try:
      token = self._read_file()
      self._set_initial_values(token)
    except FileNotFoundError:
      token = self._setup()
      self._set_initial_values(token)

  def _read_file(self):
    with open(f"{fyers_access_token_path}", "r") as f:
      token = f.read()
    return token

  def _write_file(self, token):
    with open(f"{fyers_access_token_path}", "w") as f:
      f.write(token)

  def _setup(self):
    s = requests.Session()

    data1 = f'{{"fy_id":"{self.config.username}","password":"{self.config.password}","app_id":"2","imei":"","recaptcha_token":""}}'
    r1 = s.post("https://api.fyers.in/vagator/v1/login", data=data1)
    assert r1.status_code == 200, f"Error in r1:\n {r1.json()}"

    request_key = r1.json()["request_key"]
    data2 = f'{{"request_key":"{request_key}","identity_type":"pin","identifier":"{self.config.pin}","recaptcha_token":""}}'
    r2 = s.post("https://api.fyers.in/vagator/v1/verify_pin", data=data2)
    assert r2.status_code == 200, f"Error in r2:\n {r2.json()}"

    headers = {"authorization": f"Bearer {r2.json()['data']['access_token']}", "content-type": "application/json; charset=UTF-8"}
    data3 = f'{{"fyers_id":"{self.config.username}","app_id":"{self.config.client_id[:-4]}","redirect_uri":"{self.config.redirect_uri}","appType":"100","code_challenge":"","state":"abcdefg","scope":"","nonce":"","response_type":"code","create_cookie":true}}'
    r3 = s.post("https://api.fyers.in/api/v2/token", headers=headers, data=data3)
    assert r3.status_code == 308, f"Error in r3:\n {r3.json()}"

    parsed = urlparse(r3.json()["Url"])
    auth_code = parse_qs(parsed.query)["auth_code"][0]

    session = accessToken.SessionModel(client_id=self.config.client_id, secret_key=self.config.secret_key, redirect_uri=self.config.redirect_uri, response_type="code", grant_type="authorization_code")
    session.set_token(auth_code)
    response = session.generate_token()
    token = response["access_token"]
    self._write_file(token)

    return token
