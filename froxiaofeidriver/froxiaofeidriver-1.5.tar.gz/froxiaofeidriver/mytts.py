import pyttsx3

class Pyttsx:
    tts_obj = pyttsx3.init("espeak")
    tts_obj.setProperty("voice","zh")
    tts_obj.setProperty("volume",0.5)
    tts_obj.setProperty("rate",170)
    def __init__(self):
        pass
    def my_say(self,word):
        self.tts_obj.say(word)
        self.tts_obj.runAndWait()
    def my_voice(self,volume,rate):
        self.tts_obj.setProperty("volume",volume)
        self.tts_obj.setProperty("rate",rate)


