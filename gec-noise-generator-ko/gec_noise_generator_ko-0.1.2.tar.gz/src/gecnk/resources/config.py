from __future__ import absolute_import
import configparser

# 설정파일 만들기
config = configparser.ConfigParser()

# 설정파일 오브젝트 만들기
config['system'] = {}
config['system']['max_error'] = "2"

with open('config.ini', 'w', encoding='utf-8') as configfile:
    config.write(configfile)
configfile.close