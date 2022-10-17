class findText:
    """
    This class find word a text
    """
    def __init__(self, text, word_find):
        """
        init parametres
        :param text: text to fin word
        :param word_find:  word to find
        """

        self.text = text
        self.word = word_find

    def find(self):
        """
        Returns True if word in text or False of word don't in text
        :return: bool condition
        """

        text = self.text
        word = self.word

        position = text.find(word)

        if position > -1:
            coincidence = 1
        else:
            coincidence = 0

        return coincidence
