from google.cloud import translate
from os_translator.modules import translator_boilerplate as bp


###########################################################################
# this module aim is to translate text.
###########################################################################

def translate_text(service_account_json_path,
                   project_id,
                   text,
                   language_initials_dest,
                   language_initials_src='en-US'
                   ):
    """Will translate a text to a given language.

    Parameters:
        service_account_json_path: the path to your google translate api json key. Download from your firebase's project's settings
        project_id: your project id (fetch from your api console project's name: https://console.cloud.google.com/?_ga=2.55756075.1423406147.1582784765-1154152733.1582784765)
        text: the text to translate
        language_initials_dest: the initials of the language you want to translate to
        language_initials_src: the source language

    NOTICE:
        If there are substrings you don't want to translate, write KEEP before them. Example: "The boy looks KEEPWord"
    """

    # Instantiates the client
    translate_client = translate.TranslationServiceClient.from_service_account_json(service_account_json_path)

    # translate the sentence
    return bp.translate_sentence(translate_client,
                                 project_id,
                                 language_initials_src,
                                 language_initials_dest,
                                 text)
