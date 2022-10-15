#!/usr/bin/python
import json
import os
import re
import sys

import click
from google.cloud import translate_v2
from google.oauth2 import service_account

source = 'fr'
DEFAULT_LANGUAGES = ['en', 'de', 'ko']

"""
    Translate text to a target language
    exclude params
    :arg text - text to translate
    :arg target - target language
    :return translated text
"""


def translate(text, target, translate_client):
    # Find translate params
    params = re.findall(r"{{\w+}}", text)
    for param in params:
        parsedParam = param.replace(
            '{{', '<span translate="no">').replace('}}', '</span>')
        # no translate params
        text = text.replace(param, parsedParam)

    return translate_client.translate(text, target_language=target)


"""
    Translate all values from dictionary data to language dest
    :argument
        data: dictionary
        language: language dest
    :return
        translated dictionary
"""


def translateToLanguage(data, language, translate_client):
    for key in data.keys():
        if isinstance(data[key], str):
            value = data[key]
            translation = translate(value, language, translate_client)
            data[key] = translation['translatedText'].replace(
                '<span translate="no">', '{{').replace('</span>', '}}')
        else:
            translateToLanguage(data[key], language, translate_client)


def silentremove(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")


def writeTranslateFile(data, language, output):
    # delete old version file
    silentremove(output + '/' + language + '.json')
    with open(output + '/' + language + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json_file(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


@click.command(help=f"""
Translate all the value of a json file in a language given in
argument using the google translate
API. The supported language are English, Deutsch, Korean and French.
""")
@click.option('--credentials', '-c', type=str,
              help='google key credentials file')
@click.option('--input', '-i', type=str,
              help='path to the json file to translate')
@click.option('--output', '-o', type=str,
              help='path to the json file translated')
@click.option('--languages', '-l', type=str, help="""the language to translate
              must be 'en', 'de' or 'ko'""",
              multiple=True)
@click.option('--available', '-a',
              is_flag=True, default=False,
              help="List available languages")
def json_translator(
        credentials,
        input,
        output,
        languages=DEFAULT_LANGUAGES,
        available=False
):
    credentials_dist = service_account.Credentials \
        .from_service_account_info(read_json_file(credentials))
    translate_client = translate_v2.Client(credentials=credentials_dist)

    if available:
        results = translate_client.get_languages()

        for language in results:
            print(u"{name} ({language})".format(**language))

        sys.exit(2)

    for language in languages:
        data = read_json_file(input)
        translateToLanguage(data, language, translate_client)
        writeTranslateFile(data, language, output)
