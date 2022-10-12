import socket
import requests

from hashlib import sha1
from random import random
from urllib import parse
from datetime import datetime, timedelta
from dateutil import parser as dateparser

class Auth():
	__logger = None
	__env = None

	__grant_type = None
	__auth_endpoint = None
	__token_endpoint = None
	__base_url = None
	__start_session_endpoint = None
	__verify_ssl = None

	def env(self):
		return self.__env

	def base_url(self):
		return self.__base_url

	def __init__(self, config, logger, env):

		self.__logger = logger
		self.__env = env

		try:
			self.__grant_type = config.get('OAUTH_GRANT_TYPE', env)
		except Exception as e:
			raise Exception("Failed to get 'OAUTH_GRANT_TYPE': %s" % (str(e)))

		try:
			self.__auth_endpoint = config.get('AUTH', 'OauthEndpoints')
		except Exception as e:
			raise Exception("Failed to get OauthEndpoints 'AUTH': %s" % (str(e)))

		try:
			self.__code_redirect_endpoint = config.get('CODE_REDIRECT', 'OauthEndpoints')
		except Exception as e:
			raise Exception("Failed to get OauthEndpoints 'CODE_REDIRECT': %s" % (str(e)))

		try:
			self.__token_redirect_endpoint = config.get('TOKEN_REDIRECT', 'OauthEndpoints')
		except Exception as e:
			raise Exception("Failed to get OauthEndpoints 'TOKEN_REDIRECT': %s" % (str(e)))

		try:
			self.__token_endpoint = config.get('TOKEN', 'OauthEndpoints')
		except Exception as e:
			raise Exception("Failed to get OauthEndpoints 'TOKEN': %s" % (str(e)))

		try:
			self.__revoke_endpoint = config.get('REVOKE', 'OauthEndpoints')
		except Exception as e:
			raise Exception("Failed to get OauthEndpoints 'REVOKE': %s" % (str(e)))

		try:
			self.__base_url = config.get('BASE_URL', env)
		except Exception as e:
			raise Exception("Failed to get 'BASE_URL' from %s: %s" % (env, str(e)))

		try:
			self.__start_session_endpoint = config.get('START_SESSION','API')
			self.__logger.debug("__start_session_endpoint: %s" % (self.__start_session_endpoint))
		except Exception as e:
			raise Exception("Failed to get 'START_SESSION' API endpoint: %s" % (str(e)))

		try:
			self.__audit_endpoint = config.get('AUDIT','API')
			self.__logger.debug("__audit_endpoint: %s" % (self.__start_session_endpoint))
		except Exception as e:
			raise Exception("Failed to get 'AUDIT' API endpoint: %s" % (str(e)))

		try:
			self.__verify_ssl = config.get('REQUEST_SSL_VERIFY', env, bool)
			self.__logger.debug("verify_ssl: %s" % (self.__verify_ssl))
		except Exception as e:
			self.__logger.debug("Failed to get 'REQUEST_SSL_VERIFY' for %s: %s\nDefaulting to True" % (env, str(e)))

	def setup_session(self, creds):
		try:
			self.__logger.debug("Initiating a new user auth session")
	
			params = {
				'hostname': socket.gethostname(),
				'auth_type': self.__grant_type,
			}
			params = parse.urlencode(params)

			url = self.__base_url + self.__start_session_endpoint
			resp = requests.post(url=url, params=params, verify=self.__verify_ssl)
			resp.raise_for_status()

		except Exception as e:
			raise Exception("Failed to setup_session (post, %s%s, %s): %s" % \
					(self.__base_url, self.__start_session_endpoint, params, str(e)))

		try:
			# json format
			response_data = resp.json()
			self.__logger.debug("session data: %s" % (response_data))
	
			# validate
			if 'auth_url' not in response_data or not response_data['auth_url']:
				raise Exception('invalid session data')
			if 'id' not in response_data or not response_data['id']:
				raise Exception('invalid session data')
		except Exception as e:
			self.__logger.error("Failed to setup session: %s" % (str(e))) 
			return None

		# update user credentials
		try:
			creds.add_or_update_cred('id', response_data['id'])
			creds.add_or_update_cred('auth_url', response_data['auth_url'])
		except Exception as e:
			self.__logger.warning("Failed to update user credentials: %s" % (str(e))) 

		# manual user auth
		try:
			msg = "Visit the site below in your browser, follow the steps to authenticate, " + \
						"and then come back here to continue [ENTER]\n\t%s" % (response_data['auth_url']) 
			input(msg)
		except Exception as e:
			self.__logger.error("Failed to setup session: %s" % (str(e))) 
			return None

	def get_auth_code(self, creds):
		try:
			state = sha1(str(random()).encode('utf-8')).hexdigest()
			params = {
				'client_id': creds.get_cred('id'),
				'response_type': 'code',
				'scope': 'audit',
				'state': state,
			}
			params = parse.urlencode(params)

			url = self.__base_url + self.__auth_endpoint
			self.__logger.debug("POST url %s params: %s" % (url, params))

			resp = requests.post(url=url, params=params, verify=self.__verify_ssl)
			resp.raise_for_status()
		except Exception as e:
			self.__logger.error("get_auth_code(%s:%s): %s" % \
					(self.__base_url, self.__auth_endpoint, str(e)))
			return

		try:
			# json format
			response_data = resp.json()
			self.__logger.debug("auth code response: %s" % (response_data))
	
			# validate response
			if 'state' not in response_data or response_data['state'] != state:
				raise Exception('Invalid state!')
			if 'code' not in response_data or not response_data['code']:
				raise Exception('Invalid code!')
		except Exception as e:
			self.__logger.error("Failed to get auth code: %s" % (str(e)))
			return

		try:
			# remove stale auth code/token
			creds.delete_cred('token')
			creds.add_or_update_cred('code', response_data['code'])
		except Exception as e:
			self.__logger.warning("Failed to update user credentials: %s" % (str(e))) 
	
	def get_auth_token(self, creds):
		try:
			client_id = creds.get_cred('id')
			if not client_id:
				raise Exception('no client_id')

			auth_code = creds.get_cred('code')
			if not auth_code:
				raise Exception('no auth_code')

			params = {
				'client_id': client_id,
				'code': auth_code,
				'grant_type': 'authorization_code',
				'redirect_uri': self.__code_redirect_endpoint,
			}
			params = parse.urlencode(params)
	
			url = self.__base_url + self.__token_endpoint

			self.__logger.debug("POST url: %s params: %s" % (url, params))
			resp = requests.post(url=url, params=params, verify=self.__verify_ssl)
			resp.raise_for_status()
		except Exception as e:
			self.__logger.error("get_auth_token(%s:%s): %s" % \
					(self.__base_url, self.__token_endpoint, str(e)))
			return

		try:
			# json format
			response_data = resp.json()
			self.__logger.debug("auth token: %s" % (response_data))
	
			# validate response
			if 'access_token' not in response_data or not response_data['access_token']:
				raise Exception('Invalid token!')
			if 'refresh_token' not in response_data or not response_data['refresh_token']:
				raise Exception('Invalid token!')
			if 'token_type' not in response_data or not response_data['token_type']:
				raise Exception('Invalid token!')
	
			# token expiry
			if 'expires' not in response_data:
				if 'expires_in' in response_data:
					expires_in = int(response_data['expires'])
				else:
					expires_in = 3600
				expires = datetime.now() + timedelta(seconds=expires_in)
				expires = expires.strftime('%Y-%m-%d %H:%M:%S %Z')
				response_data['expires'] = expires
		except Exception as e:
			self.__logger.error("Failed to get auth token: %s" % (str(e)))
			return
	
		# remove stale auth code/token
		creds.add_or_update_cred('token', response_data)
	
	def get_auth_implicit_token(self, creds):
		self.__logger.debug('get_auth_implicit_token')

		try:
			client_id = creds.get_cred('id')
			if not client_id:
				raise Exception('no client_id!')

			state = sha1(str(random()).encode('utf-8')).hexdigest()
			params = {
				'client_id': client_id,
				'response_type': 'token',
				'scope': 'audit',
				'state': state,
				'redirect_uri': self.__base_url + self.__token_redirect_endpoint + '/' + client_id,
			}

			params = parse.urlencode(params)
			url = self.__base_url + self.__auth_endpoint
			self.__logger.debug("(implicit) POST url: %s params: %s" % (url, params))

			resp = requests.post(url=url, params=params, verify=self.__verify_ssl)
			resp.raise_for_status()
		except Exception as e:
			raise Exception("get_auth_implicit_token(%s:%s): %s" % \
					(self.__base_url, self.__auth_endpoint, str(e)))

		try:
			# validate response
			response_data = resp.json()
			self.__logger.debug("server response: %s" % (response_data))

			assert 'error' not in response_data, response_data['error']
			if 'state' in response_data:
				response_data['state'] == state, 'Invalid state!'
		except Exception as e:
			raise Exception("get_auth_implicit_token(%s:%s): %s" % \
					(self.__base_url, self.__auth_endpoint, str(e)))

		try:	
			# token expiry
			if 'expires' not in response_data:
				if 'expires_in' in response_data:
					expires_in = int(response_data['expires'])
				else:
					expires_in = 3600
				expires = datetime.now() + timedelta(seconds=expires_in)
				expires = expires.strftime('%Y-%m-%d %H:%M:%S %Z')
				response_data['expires'] = expires
		except Exception as e:
			self.__logger,warning("get_auth_implicit_token(%s:%s): failed to add token expiry (%s)" % \
					(self.__base_url, self.__auth_endpoint, str(e)))

		try:
			# remove stale auth code/token
			creds.delete_cred('code')
			creds.add_or_update_cred('token', response_data)
		except Exception as e:
			self.__logger.warning("get_auth_implicit_token(%s:%s): failed to save token (%s)" % \
					(self.__base_url, self.__auth_endpoint, str(e)))

	def authorize_audit_request(self, body, creds):
		try:
			token = creds.get_cred('token')
			assert token, "No access token!"

			if self.__grant_type == 'code':
				header = {
					"Authorization": f"{token['token_type']} {token['access_token']}"
				}
			else:
				header = {
					"Authorization": f"{token['type']} {token['access_token']}"
				}

			params = parse.urlencode(body)
			url = self.__base_url + self.__audit_endpoint
			resp = requests.post(url=url, params=params, headers=header, verify=self.__verify_ssl)
			resp.raise_for_status()

			try:
				resp_data = resp.json()
			except:
				resp_data = resp.content
			return resp_data
		except Exception as e:
			raise Exception("Failed to authorize request: %s" % (str(e)))

	def refresh_credentials(self, creds):
		try:
			self.__logger.debug("Refreshing user auth tokens")

			client_id = creds.get_cred('id')
			if not client_id:
				raise Exception("refresh_credentials(): failed to get client_id!")

			state = sha1(str(random()).encode('utf-8')).hexdigest()
	
			token = creds.get_cred('token')
			if not token:
				raise Exception("refresh_credentials(): failed to get tokens!")

			refresh_token = token['refresh_token']
	
			params = {
				'client_id': client_id,
				'grant_type': 'refresh_token',
				'scope': 'audit',
				'refresh_token': refresh_token,
				'state': state,
			}
			params = parse.urlencode(params)
	
			url = self.__base_url + self.__token_endpoint
		except Exception as e:
			raise Exception("Error constructing refresh request: %s" % (str(e)))

		self.__logger.debug("POST url: %s params: %s" % (url, params))

		try:
			# talk to the server
			resp = requests.post(url=url, params=params, verify=self.__verify_ssl)
			resp.raise_for_status()
		except Exception as e:
			self.__logger.debug("Failed to refresh tokens: %s" % (str(e)))
			raise Exception("Server error: %s" % (str(e)))

		try:
			# validate response
			response_data = resp.json()
		except Exception as e:
			raise Exception("Invalid data: %s" % (str(e)))

		self.__logger.debug("refresh response: %s" % (response_data))
		if 'state' in response_data and response_data['state'] != state:
			raise Exception('Invalid state!')
	
		try:
			# token expiry
			if 'expires' not in response_data:
				if 'expires_in' in response_data.keys():
					expires_in = int(response_data['expires'])
				else:
					expires_in = 3600
				expires = datetime.now() + timedelta(seconds=expires_in)
				expires = expires.strftime('%Y-%m-%d %H:%M:%S %Z')
				response_data['expires'] = expires
		except Exception as e:
			self.__logger.debug("Failed to parse token expiry: %s" % (str(e)))

		try:
			creds.add_or_update_cred('token', response_data)
		except Exception as e:
			self.__logger.debug("Failed to save tokens: %s" % (str(e)))
	
	def token_expired(self, creds, token):
		expired = False
		if not token:
			token = creds.get('token')
		if token:
			expiry = dateparser.parse(token['expires'])
			current_time = datetime.now(expiry.tzinfo)
			if expiry < current_time:
				expired = True
			self.__logger.debug("Token expiry %s current_time %s (expired: %s)" % \
					  (expiry, current_time, expired))
		return expired
	
	def create_or_refresh_session(self, creds, expired=False):
		self.__logger.debug("create_or_refresh_session(expired: %s) grant_type: %s" % \
				(expired, self.__grant_type))

		if expired and self.__grant_type == 'code':
			try:
				self.refresh_credentials(creds)
				return
			except Exception as e:
				if '401 Client Error: UNAUTHORIZED for url' in str(e):
					if self.__env == "Staging":
						print("Failed to refresh user credentials:: request not supported!")
						exit(1)
					expired = True
				else:
					print("Failed to refresh user credentials: %s! Exiting." % (str(e)))
					exit(1)
	
		if expired:
			self.__logger.debug('FATAL: Access token has expired. Please re-authenticate the user.')

		if self.__grant_type == 'code':
			# create a new auth session
			try:
				self.setup_session(creds)
			except Exception as ee:
				print("Failed to initiate authentication session: %s. Exiting!" % (str(ee)))
				exit(1)

		# continue with user authentication
		try:
			if self.__grant_type == 'token':
				self.get_auth_implicit_token(creds)
			else:
				self.get_auth_code(creds)
				self.get_auth_token(creds)
		except Exception as e:
			print("Failed to authenticate: %s! Exiting." % (str(e)))
			exit(1)

####################################
# Main
####################################
if __name__ == "__main__":
	test
