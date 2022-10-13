import speech_recognition as sr
import pyttsx3
def lekho(variable):
    print(f'{variable}')
def bolo(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def shuno():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit= 5)
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Apni bolechen:\n {query}")
    except Exception as e:
        return 'none'
    return query

def input_nao(input_variable):
    input(f'{input_variable}')


def hishab_koro_rectangular_area(l,w):
    print("The area is", l*w)
def hishab_koro_square_area(a):
    print("The area is", a*a)
def hishab_koro_triangle_area(l,h):
    print("The are is", 0.5*l*h)
def hishab_koro_circular_area_diametre(d):
    r = 0.5*d
    print("The area is", 3.1416*r*r)
def hishab_koro_circular_area_radius(r):
    print("The area is", 3.1416*r*r)
def hishab_kore_bolo_rectangular_area(l,w):
    bolo("The area is")
    bolo(l*w)
def hishab_kore_bolo_square_area(a):
    bolo("The area is")
    bolo(a*a)
def hishab_kore_bolo_triangle_area(l,h):
    bolo("The area is")
    bolo(0.5*l*h)
def hishab_kore_bolo_circular_area_diametre(d):
    r = 0.5*d
    bolo("The area is")
    bolo(3.1416*r*r)
def hishab_kore_bolo_circular_area_radius(r):
    bolo("The area is")
    bolo(3.1416*r*r)
def sum(x,y):
    result = x+y
    lekho(result)
