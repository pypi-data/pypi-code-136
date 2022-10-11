class Answer:
    def __init__(self, fraction, text, feedback):
        self.fraction = fraction
        self.text = text
        self.feedback = feedback

    def __init__(self):
        self.fraction = None
        self.text = ""
        self.feedback = ""

    def setfraction(self, fraction):
        self.fraction = fraction

    def settext(self, text):
        self.text = text

    def setfeedback(self, feedback):
        self.feedback = feedback
