class LanguageCodes:
    hindi = 'hi'
    hinglish = 'hi-en'

    def get_all_language_codes(self):
        return [self.hindi, self.hinglish]


class LMConfigs:
    all_language_codes = LanguageCodes()
    tokenizer_model_file_url = {
        all_language_codes.hindi: 'https://www.dropbox.com/s/xrsjt8zbhwo7zxq/hindi_lm.model?raw=1',
        all_language_codes.hinglish: 'https://www.dropbox.com/s/oblv8oalv5lwdec/tokenizer.model?raw=1',
    }

    def __init__(self, language_code: str):
        self.language_code = language_code

    def get_config(self):
        return {
            'tokenizer_model_url': self.tokenizer_model_file_url[self.language_code],
            'tokenizer_model_file_name': 'tokenizer.model'
        }