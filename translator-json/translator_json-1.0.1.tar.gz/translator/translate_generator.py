#!/usr/bin/python
import json
import os
import re

import click
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"translator/googlekey.json"

translate_client = translate_v2.Client()

source = 'fr'
DEFAULT_LANGUAGES = ['en', 'de', 'ko']

"""
    Translate text to a target language
    exclude params
    :arg text - text to translate
    :arg target - target language
    :return translated text
"""


def translate(text, target):
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


def translateToLanguage(data, language):
    for key in data.keys():
        if isinstance(data[key], str):
            value = data[key]
            translation = translate(value, language)
            data[key] = translation['translatedText'].replace(
                '<span translate="no">', '{{').replace('</span>', '}}')
        else:
            translateToLanguage(data[key], language)


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


@click.command(help=f"""
Translate all the value of a json file in a language given in
argument using the google translate
API. The supported language are English, Deutch, Korean and French.
""")
@click.option('--source', '-s', type=str,
              help='path to the json file to translate',
              required=True)
@click.option('--output', '-o', type=str,
              help='path to the json file translated',
              required=True)
@click.option('--languages', '-l', type=str, help="""the language to translate
              must be 'en', 'de' or 'ko'""",
              multiple=True)
def json_translator(source, output, languages=DEFAULT_LANGUAGES):
    for language in languages:
        f = open(source)
        data = json.load(f)
        f.close()
        translateToLanguage(data, language)
        writeTranslateFile(data, language, output)
