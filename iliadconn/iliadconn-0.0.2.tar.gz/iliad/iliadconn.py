import os
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
from dateutil.relativedelta import relativedelta
import configparser
import tempfile
import appdirs

ILIAD_URL = 'https://www.iliad.it/account/consumi-e-credito'
CONFIG_FILE = 'iliadconn.ini'
TMP_DEBUG_FILE = 'iliadconn_debug.json'
TMP_DATA_FILE = 'iliadconn_data.json'


class ScrapingException(Exception):
    pass


class MaintenanceException(Exception):
    pass


class LoginException(Exception):
    pass


def config():
    cfg = configparser.ConfigParser()
    if sys.platform == 'linux':
        os.environ['XDG_CONFIG_DIRS'] = '/etc:/usr/local/etc'
    cfg_dirs = appdirs.site_config_dir('iliad', multipath=True).split(':')
    cfg_dirs.append(appdirs.user_config_dir('iliad'))
    cfg_dirs.append(os.path.dirname(os.path.abspath(__file__)))
    cfg_dirs.reverse()
    for d in cfg_dirs:
        cfg_file_path = os.path.join(d, CONFIG_FILE)
        cfg.read(cfg_file_path)
        if 'iliad.it' in cfg:
            user = cfg['iliad.it']['user']
            password = cfg['iliad.it']['password']
            if user == '<INSERT_USER>' and password == '<INSERT_PASSWORD>':
                print(f'insert your credentials in {cfg_file_path}')
                return
            return user, password
    else:
        cfg_file_path = os.path.join(appdirs.user_config_dir('iliad'), CONFIG_FILE)
        try:
            cfg['iliad.it'] = {'user': '<INSERT_USER>', 'password': '<INSERT_PASSWORD>'}
            if not os.path.exists(cfg_file_path):
                os.makedirs(os.path.dirname(cfg_file_path))
            with open(cfg_file_path, 'w') as configfile:
                cfg.write(configfile)
            print(f"config auto created on {cfg_file_path}")
        except Exception as e:
            print(f"failed config read, error '{str(e)}' to auto-create empty config: {cfg_file_path}")


def scrap(user, password):
    s = requests.Session()
    # get necessary for set cookies
    # <RequestsCookieJar[<Cookie ACCOUNT_SESSID=k5hkthg4612ch1pqoc8ek02oh1 for www.iliad.it/account/>,
    # <Cookie auth_mobile=1 for www.iliad.it/account/>]>
    s.get(ILIAD_URL)
    login_resp = s.post(ILIAD_URL, data={'login-ident': user, 'login-pwd': password})
    if login_resp.status_code != 200 or login_resp.text.count('ID utente o password non corretto'):
        raise LoginException()
    markup = login_resp.content
    bs4parser = BeautifulSoup(markup, "lxml")
    # noinspection PyBroadException
    try:
        cons = bs4parser.findAll('div', {'class': 'conso__text'})[2].text.strip().split('\n')[0].upper()
        date_next_subscription = bs4parser.findAll('div', {'class': 'end_offerta'})[0].text.strip().split(' ')[-1]
        date_next_subscription = datetime.strptime(date_next_subscription, '%d/%m/%Y')  # 19/06 (day/month)
        consumed = cons.split('/')[0].strip().replace(',', '.').replace('GB', '')
        total_max = int(cons.split('/')[1].strip().replace('GB', '').replace(',', '.'))
    except Exception:
        if bs4parser.text.count('maintenance') or bs4parser.text.count('manutenzione'):
            # noinspection PyBroadException
            try:
                with open(os.path.join(tempfile.gettempdir(), TMP_DATA_FILE), 'r') as f:
                    old_data = json.loads(f.read())
                    return old_data['date_next_subscription'], old_data['consumed'], old_data['total_max'], True
            except Exception:
                raise MaintenanceException()
        else:
            raise ScrapingException()
    if consumed.count('MB'):
        consumed = consumed.replace('MB', '')
        consumed = float(consumed) / 1000
    else:
        consumed = float(consumed)
    with open(os.path.join(tempfile.gettempdir(), TMP_DATA_FILE), 'w') as f:
        f.write(json.dumps({'date_next_subscription': date_next_subscription.isoformat(),
                            'consumed': consumed,
                            'total_max': total_max,
                            'date': datetime.now().isoformat()}))
    return date_next_subscription, consumed, total_max, False


def calc_forecast(date_next_subscription, consumed, total_max, maintenance):
    date_now = datetime.now().date()
    delta_month = date_next_subscription.month - date_now.month
    date_end_current_subscription = date_next_subscription - relativedelta(months=delta_month)
    date_start_current_subscription = date_end_current_subscription - relativedelta(months=1)
    days_passed = (date_now - date_start_current_subscription.date()).days or 1
    days_next = (date_end_current_subscription.date() - date_now).days
    avg_consumed_day = consumed / days_passed
    with open(os.path.join(tempfile.gettempdir(), TMP_DEBUG_FILE), 'w') as f:
        f.write(json.dumps({'avg_consumed_day': avg_consumed_day,
                            'days_passed': days_passed,
                            'days_next': days_next,
                            'date_start_current_subscription': date_start_current_subscription.isoformat(),
                            'date_end_current_subscription': date_end_current_subscription.isoformat(),
                            'date': datetime.now().isoformat()}))
    expectation = round(consumed + (avg_consumed_day * days_next))
    expectation_resp = '\u2713' if expectation < total_max else '\u26A0'
    if maintenance:
        expectation_resp = '?'
    return f'iliad: {consumed}/{total_max}GB ({expectation}GB/m {expectation_resp})'


def main():
    cfg = config()
    if cfg:
        user, password = cfg
        if not user or not password:
            exit(-1)
        try:
            date_next_subscription, consumed, total_max, maintenance = scrap(user, password)
            print(calc_forecast(date_next_subscription, consumed, total_max, maintenance))
        except ScrapingException:
            print('fatal error, fail scraping')
        except MaintenanceException:
            print('on maintenance')
        except LoginException:
            print('login failed')


if __name__ == "__main__":
    main()
