from bru_analysis.common.find_text import findText

text = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los " \
       "de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. "

word = "lugar"

coincidence = findText(text=text, word_find=word).find()

print(coincidence)

words = ['lugar', 'perro', 'astillero']

list_coincidence = []
for i in words:
    temp1 = findText(text=text, word_find=i).find()
    list_coincidence.append(temp1)

print(list_coincidence)
