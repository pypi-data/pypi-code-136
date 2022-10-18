import os
import json


def test1():
    import requests
    print('hogehoge')


def test2():
    print('hogefuga')


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
# 認証ファイルがある階層を引数でセット
def gcp_secret_manager(secret_file_folder_path):
    # ローカルで実行
    if os.name == 'nt':
        google_seacret_path = f'{secret_file_folder_path}/service_account.json'
        env_variable_path = f'{secret_file_folder_path}/env.json'

        # GCP認証用のファイルパス
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_seacret_path
        
        # JSONから環境変数をセット
        with open(env_variable_path, "r") as file:
            dict = json.load(file)
            for key, value in dict.items():
                os.environ[key] = value

    # クラウドファンクションで実行
    elif os.name == 'posix':
        google_seacret_path = '/secret/gcp_service_account'
        env_variable_path = '/secret/env'

        # GCP認証用のファイルパス
        with open(google_seacret_path, 'r', encoding='utf-8') as f:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f.read()
        
        # JSONから環境変数をセット
        with open(env_variable_path, "r") as file:
            dict = json.load(file)
            for key, value in dict.items():
                os.environ[key] = value
    
    return google_seacret_path


# GCPの認証を戻す関数
def generate_google_service_auth(service):
    from oauth2client.service_account import ServiceAccountCredentials
    import gspread

    if service == "spreadsheet":
        a_api = 'https://spreadsheets.google.com/feeds'
        b_api = 'https://www.googleapis.com/auth/drive'
        SCOPES = [a_api, b_api]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            gcp_secret_manager(), SCOPES)

        google_service_auth = gspread.authorize(credentials)
    else:
        print("サービス未選択")
        return False

    return google_service_auth


# Feedly のアクセストークンを返す
def generate_feedly_token():
    import requests

    gcp_secret_manager()
    url = 'https://cloud.feedly.com/v3/auth/token'
    params = {
        'client_id': 'feedlydev',
        'client_secret': 'feedlydev',
        'grant_type': 'refresh_token',
        'refresh_token': os.environ['FEEDLY_REFRESH_TOKEN'],
    }

    headers = {
        'Content-Type': 'application/json',
    }

    res = requests.post(url, headers=headers, params=params).json()
    return res['access_token']


# 現在日時情報の取得
# 引数のサンプル '%Y/%m/%d'
def make_date_info(format):
    from datetime import datetime, timedelta, timezone
    JST = timezone(timedelta(hours=+9), 'JST')
    dt_now_name = datetime.now(JST).strftime(format)
    return dt_now_name

# クラウドストレージへのアップロード
# bucket > アップロードしたいストレージのバスケット名
# blob > バスケット名を除く､アップロード対象のパス
def uplaod_storage(bucket_name, blob_path, upload_file_path):
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(upload_file_path)
    return f'https://storage.cloud.google.com/{bucket_name}/{blob_name}?authuser=1'


# クラウドストレージからのダウンロード
# bucket > ストレージのバスケット名
# blob > バスケット名を除く､ダウンロード先のパス
def downlaod_storage(bucket_name, blob_path, download_file_path):
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.download_to_filename(download_file_path)
    return download_file_path