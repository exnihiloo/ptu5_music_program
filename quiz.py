from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):
        # nustatome klausimų skaičių į 0
        self.klausimai = 0
        # nustatome rodomus klausimus
        self.rodyti_klausima()
        # pasirinktas_ats laiko int reikšmę, kuri naudojama
        # pasirinktoms klausimų opcijoms.
        self.pasirinktas_ats = IntVar()
        # roddysime radio buttons esamam klausimui
        # ir pateiksime klausimus prie radio button
        self.opcija = self.radio_buttons() 
        # rodysim pasiirnkimus klausimui
        self.rodyti_pasirinkimus()
        # "Kitas" ir "išeiti mygtukai"
        self.mygtukai()
        # nustatome klausimų kiekį. question yra iš data.json failo
        self.viso_klausimu = len(question)
        # skaičiuosime teisingus atsakymus.
        self.teisingi = 0

    def mygtukai(self):
        pass

    def rodyti_klausima(self):
        pass

    def rodyti_pasirinkimus(self):
        pass

    def radio_buttons(self):
        pass














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