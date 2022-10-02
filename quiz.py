from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):















langas = Tk()
langas.geometry("550x350")
langas.title("\U0001F3A7 Music Quiz")
# gauname duomenis iš json failo
with open('data.json') as failas:
    data = json.load(failas)
 
# nustatome klausimus, pasirinkimus ir atsakymus, kurie yra json faile
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

quiz = Quiz()
langas.mainloop()