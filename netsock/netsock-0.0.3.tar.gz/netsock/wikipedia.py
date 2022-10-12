import wikipedia as wpd

class Wikipedia:
      def setlang(self, language):
            self.language = language
            wpd.set_lang(self.language)

      def search(self, page, *args):
            return wpd.search(page, *args)

      def suggest(self, page):
            return wpd.suggest(page)

      def find(self, page, *args):
            return wpd.summary(page, *args)
      def page(self, page):
            return wpd.page(page)

      def languages(self):
            return wpd.languages()


      