from translate import Translator as trs

class Translator:
      def __init__(self):
            self.from_lang = None
            self.to_lang = None
            self.text = None

      def translate(self):
            translator = trs(from_lang=self.from_lang, to_lang=self.to_lang)
            translation = translator.translate(self.text)

            return translation      