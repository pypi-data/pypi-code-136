import os


def test1():
    import requests
    print('hogehoge')


def test2():
    print('hogehoge')


# Twitterで利用
# v1.1 に対応
def generate_twitter_api(CK, CKS, AT, ATS):
    import tweepy
    auth = tweepy.OAuthHandler(CK, CKS)
    auth.set_access_token(AT, ATS)

    return tweepy.API(auth, wait_on_rate_limit=True)


# GCPで利用
# 認証キーの取得に利用
# リソースIDのコピーから取得可能
def gcp_secret_manager():
    if os.name == 'nt':
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'E:/WorkSpace/Codes/service_account.json'
    elif os.name == 'posix':
        file_path = '/secret/gcp_service_account'
        with open(file_path, 'r', encoding='utf-8') as f:
            secret = f.read()
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = secret
