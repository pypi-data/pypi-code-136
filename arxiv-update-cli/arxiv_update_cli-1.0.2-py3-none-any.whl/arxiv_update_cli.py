#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2022 Juliette Monsel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import tempfile
import configparser
from datetime import datetime, timedelta
from time import mktime
import argparse
import os
import sys
import smtplib
import ssl
import getpass
import signal
import re
from email.message import EmailMessage
import logging

import feedparser


VERSION = "1.0.2"


# --- logging setup
PATH_LOG = os.path.join(tempfile.gettempdir(), "arxiv_update_cli.log")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)-15s %(levelname)s: %(message)s',
                    filename=PATH_LOG)
logging.getLogger().addHandler(logging.StreamHandler())

# --- input with timeout
TIMEOUT = 60

def timedout(signum, frame):
    raise TimeoutError(f'No input after {TIMEOUT}s.')


signal.signal(signal.SIGALRM, timedout)


def input_timeout(prompt="", timeout=TIMEOUT):
    """Input with timeout."""
    signal.alarm(timeout)
    text = input(prompt)
    signal.alarm(0)       # remove alarm
    return text


# --- default config file
default_config = {
    "General": {
        "categories": "quant-ph",  # comma separated values, e.g. "quant-ph,cond-mat.mes-hall"
        "#categories": "comma separated values, e.g. quant-ph, cond-mat.mes-hall",
        "keywords": "",
        "#keywords": "comma separated list, e.g. machine learning, optomechanics",  # comment
        "authors": "",
        "#authors": "comma separated list of authors to follow",  # comment
        "sort_by": "submittedDate", # or "lastUpdatedDate"
        "last_update": "",
        "#note": "The script will fetch the articles submitted/updated after the last update date that belong to one of the categories and fulfill: (one of the authors is in the author list) OR (one of the keywords is in the title or abstract)",
    },
    "Email": {
        "smtp_server": "",
        "#smtp_server": "smtp server used to send the results by email, e.g. smtp.gmail.com",
        "smtp_port": "465",
        "email": "",
        "#email": "email address to send the results by email",
    }
}
CONFIG = configparser.ConfigParser()
for section, options in default_config.items():
    CONFIG.setdefault(section, options)

# default config path
if 'linux' in sys.platform:
    # local directory containing config files
    if os.path.exists(os.path.join(os.path.expanduser("~"), ".config")):
        PATH_DEFAULT_CONFIG = os.path.join(os.path.expanduser("~"), ".config", "arxiv_update_cli.ini")
    else:
        PATH_DEFAULT_CONFIG = os.path.join(os.path.expanduser("~"), ".arxiv_update_cli")
else:
    # local directory containing config files
    path = os.path.join(os.path.expanduser("~"), "arxiv_update_cli")
    if not os.path.exists(path):
        os.mkdir(path)
    PATH_DEFAULT_CONFIG = os.path.join(path, "arxiv_update_cli.ini")


def save_config(filepath):
    with open(filepath, 'w') as file:
        CONFIG.write(file)


# --- keyring (for email sending)
try:
    import keyring
except ImportError:

    def store_pwd_in_keyring(username, pwd):
        pass

    def get_pwd_from_keyring(username):
        pass

else:
    if "linux" in sys.platform:
        try:
            # get the keyring to work when script is called from cron
            os.environ['DBUS_SESSION_BUS_ADDRESS'] = f'unix:path=/run/user/{os.getuid()}/bus'
            os.environ['DISPLAY'] = ':0'
        except Exception:
            pass

    def store_pwd_in_keyring(username, pwd):
        try:
            keyring.set_password("arxiv_update_cli", username, pwd)
        except keyring.errors.KeyringError:
            return


    def get_pwd_from_keyring(username):
        try:
            return keyring.get_password("arxiv_update_cli", username)
        except keyring.errors.KeyringError:
            return


# --- command line arguments parser
desc = """
CLI tool to fetch new articles on arXiv in selected categories filtered by
 keywords or authors. The updates can also be sent by email so that the script
 can be automatically run with cron.

The script will fetch the articles on arXiv that

 (1) were *submitted/updated* after the last update date (or the provided date)

 **AND**

 (2) belong to one of the *categories*

 **AND**

 (3) (one of the *authors* is in the author list) **OR** (one of the *keywords* is in the title or abstract)

All the *options* are set in the configuration file.

Note that keywords can contain spaces, e.g. "machine learning".

Thank you to arXiv for use of its open access interoperability.
"""

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-e', '--email', action='store_true',
                    help='send result by email (prompt for missing settings)')
parser.add_argument('-s', '--since',
                    type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                    metavar="YYYY-MM-DD",
                    help='fetch update since YYYY-MM-DD 00:00')
parser.add_argument('-c', '--config', nargs="?", const="",
                    metavar="FILE",
                    help='config file to use or print path to default one and exit if no argument is provided')
parser.add_argument('-v', '--version', help='show version and exit',
                    action='store_true')
parser.add_argument('--log', help='show path to log file and exit',
                    action='store_true')


# --- feed query
API_URL = 'http://export.arxiv.org/api/query?'


def _query(url, start=0, trial_nb=1, max_trials=10):
    """Fetch query results and retry MAX_TRIALS in case of failure."""
    res = feedparser.parse(url.format(start=start))
    if res['entries']:
        return res['entries']
    err = res.get('bozo_exception', '')
    if err:
        raise ValueError(str(err))
    tot_results = int(res['feed']['opensearch_totalresults'])
    if start < tot_results:  # entries shouldn't be empty
        if trial_nb >= max_trials:
            raise ValueError("Failed to retrieve results from API.")
        return _query(url, start, trial_nb + 1, max_trials)
    return []  # no results


def api_query(start_date):
    """Return arXiv API query results as a generator."""
    categories = "+OR+".join([cat.strip() for cat in CONFIG.get("General", "categories").split(",")])
    if not categories:
        raise ValueError("No category selected. Please edit the configuration file.")
    keywords = "+OR+".join([f'%22{kw.strip().replace(" ", "+")}%22' for kw in CONFIG.get("General", "keywords").split(",") if kw.strip()])
    authors = "+OR+".join([f'%22{auth.strip().replace(" ", "+")}%22' for auth in CONFIG.get("General", "authors").split(",") if auth.strip()])
    sort_by = CONFIG.get("General", "sort_by")
    date = datetime.now()

    args = []
    if keywords:
        # search for keywords in both title and abstract of articles in given categories
        args.append(f"%28ti:%28{keywords}%29+OR+abs:%28{keywords}%29%29")
    if authors:
        args.append(f"au:%28{authors}%29")
    if args:
        search_query = f"cat:%28{categories}%29+AND+%28{'+OR+'.join(args)}%29"
    else:
        # no filtering, get all articles from the categories
        search_query = f"cat:%28{categories}%29"

    url = f'{API_URL}search_query={search_query}' \
          f'&sortBy={sort_by}&sortOrder=descending&max_results=50' \
          '&start={start}'
    i = 0
    entries = _query(url, i, 1)
    entry = None
    while entries and date >= start_date:
        for entry in entries:
            date = datetime.fromtimestamp(mktime(entry['updated_parsed']))
            if date < start_date:
                break
            yield entry
        i += 50
        entries = _query(url, i, 1)


ansi_regexp = re.compile(r"\033\[[0-9]+m")

def send_email(txt):
    """Return True if the email is sent."""
    # SMTP server settings
    smtp_server = CONFIG.get("Email", "smtp_server", fallback="")
    port = CONFIG.getint("Email", "smtp_port")
    if not smtp_server:
        smtp_server = input_timeout("SMTP server (e.g. smtp.gmail.com): ")
        CONFIG.set("Email", "smtp_server", smtp_server)
    login = CONFIG.get("Email", "email", fallback="")
    if not login:
        login = input_timeout("email: ")
        CONFIG.set("Email", "email", login)

    password = get_pwd_from_keyring(login)
    if password is None:
        password = getpass.getpass(f"Password for {login}: ")

    # mail content
    msg = EmailMessage()
    msg.set_content(ansi_regexp.sub('', txt))
    msg['Subject'] = f"arXiv update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    msg['From'] = login
    msg['To'] = login

    # server connexion
    context = ssl.create_default_context()  # create SSL context
    trial_nb = 0
    while trial_nb < 3:
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(login, password)
                server.send_message(msg)
        except smtplib.SMTPAuthenticationError:
            trial_nb += 1
            logging.error("Authentication failed for %s", login)
            password = getpass.getpass(f"Password for {login}: ")
        except Exception:
            logging.exception("Email sending failed, please check the configuration file")
            return False
        else:
            store_pwd_in_keyring(login, password)
            logging.info("Email sent")
            return True


def _main():
    args = parser.parse_args()

    # version
    if args.version:
        print('arxiv_update_cli ', VERSION)
        sys.exit()

    # log
    if args.log:
        print("log file: ", PATH_LOG)
        sys.exit()

    # config file
    path_config = PATH_DEFAULT_CONFIG

    if args.config == "":
        print("Default config file: ", PATH_DEFAULT_CONFIG)
        sys.exit()
    elif args.config:
        # load config
        if CONFIG.read(args.config):
            path_config = args.config
        else:
            logging.warning("Invalid config file %s, default config file used instead.", args.config)

    if path_config == PATH_DEFAULT_CONFIG:
        if not CONFIG.read(path_config):
            with open(path_config, 'w') as file:
                CONFIG.write(file)
            logging.info("No configuration file found. Default configuration file '%s' has been created. "
                         "Please edit it and run the script again.", path_config)
            sys.exit()

    # start date
    now = datetime.now()
    if args.since is None:
        try:
            start_date = datetime.strptime(CONFIG.get("General", "last_update"),
                                           '%Y-%m-%d %H:%M')
        except ValueError:
            start_date = now - timedelta(days=1)
    else:
        start_date = args.since

    # run query
    results = api_query(start_date)

    # format results
    i = -1
    articles = []
    for i, article in enumerate(results):
        title = article['title'].strip().replace('\n ', '')
        date = datetime.fromtimestamp(mktime(article['updated_parsed']))
        authors = [a['name'] for a in article['authors']]
        link = article['link']
        abstract = article['summary'].splitlines()
        ref = article.get('arxiv_journal_ref')
        doi = article.get('arxiv_doi')
        comments = article.get('arxiv_comment')
        txt = [f'\033[1mTitle:\033[0m {title}',
               f'\033[1mAuthors:\033[0m {", ".join(authors)}',
               f'\033[1mDate:\033[0m {date.strftime("%Y-%m-%d %H:%M")}',
               f'\033[1mAbstract:\033[0m {" ".join(abstract)}']
        if comments:
            txt.append(f'\033[1mComments:\033[0m {comments}')
        if ref:
            txt.append(f'\033[1mJournal reference:\033[0m {ref}')
        if doi:
            txt.append(f'\033[1mDOI:\033[0m \033[36mhttps://doi.org/{doi}\033[0m')
        txt.append(f'\033[1mURL:\033[0m \033[36m{link}\033[0m')
        articles.append('\n'.join(txt) + '\n')

    footer = f"\033[3m%% {i+1} new articles since {start_date.strftime('%Y-%m-%d %H:%M')}\033[0m"
    output = "\n".join(articles)
    if not articles:
        logging.info("No new articles since %s", start_date.strftime('%Y-%m-%d %H:%M'))
        return

    cli_ouput = True
    if args.email:
        cli_ouput = not send_email(output + "\n" + footer)  # fallback to printing if email failed
    if cli_ouput:
        print(output)
    logging.info(footer)

    CONFIG.set("General", "last_update", now.strftime('%Y-%m-%d %H:%M'))
    save_config(path_config)


def main():
    try: # log exceptions
        _main()
    except Exception:
        logging.exception("An error occured")


# --- execute
if __name__ == "__main__":
    main()
