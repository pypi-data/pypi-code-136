# coding=utf-8
import sys
from google.cloud import translate

# just the boiler plate of the sentence translator
play_initials_bank = ['en-GB', 'af', 'am', 'ar', 'hy-AM', 'az-AZ', 'bn-BD', 'eu-ES', 'be', 'bg', 'my-MM', 'ca', 'zh-HK', 'zh-CN', 'zh-TW', 'hr', 'cs-CZ', 'da-DK', 'nl-NL', 'en-AU', 'en-IN', 'en-SG', 'en-ZA', 'en-CA', 'en-US', 'et', 'fil', 'fi-FI', 'fr-FR', 'fr-CA', 'gl-ES', 'ka-GE', 'de-DE', 'el-GR', 'hi-IN', 'hu-HU', 'is-IS', 'id', 'it-IT', 'ja-JP', 'kn-IN', 'km-KH', 'ko-KR', 'ky-KG', 'lo-LA', 'lv', 'lt', 'mk-MK', 'ms', 'ml-IN', 'mr-IN', 'mn-MN', 'ne-NP', 'no-NO', 'fa', 'pl-PL', 'pt-BR',
                      'pt-PT', 'ro', 'ro', 'ru-RU', 'sr', 'si-LK', 'sk', 'sl', 'es-419', 'es-ES', 'es-US', 'sw', 'sv-SE', 'ta-IN', 'te-IN', 'th', 'tr-TR', 'uk', 'vi', 'zu']


# the actual conversion of a text
def translate_sentence(translate_client, project_id, language_src, language_dest, text):
    # translate
    parent = f'projects/{project_id}'
    try:
        response = translate_client.translate_text(
            parent=parent,
            contents=[text],
            mime_type="text/plain",

            source_language_code=language_src,
            target_language_code=language_dest)

        ans = ""
        for translation in response.translations:
            ans += format(translation.translated_text)
        return ans
    except Exception as e:
        return e


# will convert play initials to translate initials
def play_for_translate(play_initials):
    translate_initials = play_initials
    if '-' in play_initials:
        translate_initials = play_initials[:play_initials.index('-')]
    return translate_initials


# will return the indexes of all of the matching substrings in a string
def find_all_substrings(string, word):
    all_positions = []
    next_pos = -1
    while True:
        next_pos = string.find(word, next_pos + 1)
        if next_pos < 0:
            break
        all_positions.append(next_pos)
    return all_positions
