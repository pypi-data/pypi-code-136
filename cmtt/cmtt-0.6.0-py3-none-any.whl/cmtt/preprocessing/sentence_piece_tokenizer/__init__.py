from fastai.text import *
from cmtt.preprocessing.sentence_piece_tokenizer.config import LanguageCodes
from cmtt.preprocessing.sentence_piece_tokenizer.download_assets import setup_language, verify_tokenizer_model
from cmtt.preprocessing.sentence_piece_tokenizer.tokenizer import IndicTokenizer

all_language_codes = LanguageCodes().get_all_language_codes()


def download(language_code: str):
    if language_code not in all_language_codes:
        print("Language not supported")
        return
    learn = setup_language(language_code)
    return learn


def download_models(language_code: str):
    if not verify_tokenizer_model(language_code):
        download(language_code)
    else:
        print("Tokenizer Model already Downloaded")


def check_input_language(language_code: str):
    if language_code not in all_language_codes:
        print("Error: Language Not Supported")
        return -1
    if not verify_tokenizer_model(language_code):
        print(f"Tokenizer model not downloaded. Run setup('{language_code}') first")
        return -1
    return 1


def tokenize(input: str, language_code: str):
    if (check_input_language(language_code)==-1):
        return

    tok = IndicTokenizer(language_code)
    output = tok.tokenizer(input)
    return output

