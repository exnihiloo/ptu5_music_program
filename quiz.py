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
        next_button = Button(langas, text="Kitas", command=self.kitas_mygtukas,
        width=15,fg="black",font=("Menlo", 16, "bold"))
        next_button.place(x=100,y=220)
        quit_button = Button(langas, text="Išeiti", command=langas.destroy,
        width=5, fg="black",font=("Menlo", 16, " bold"))
        quit_button.place(x=460,y=0)

    def rodyti_klausima(self):
        klausimai = Label(langas, text = question[self.klausimai], width=60,
        font = ('ariel', 14, 'bold' ), anchor= 'w' )
        klausimai.place(x=40, y=50)

    def rodyti_pasirinkimus(self):
        val = 0
        # nuimam taškelius nuo pasirinkimų, kai išmetamas kitas klausimas
        self.pasirinktas_ats.set(0)
        # loopinam per pasirinkimus iš json failo, kurie rodomi, kaip tekstas prie radio button
        for option in options[self.klausimai]:
            self.opcija[val]['text'] = option
            val += 1

    def radio_buttons(self):
        # sukuriam sąrašą su tuščiu pasirinkimų sąrašu
        q_list = []
        # pirmo pasirinkimo pozicija lange
        y_pos = 90
        # pridedame pasirinkimus į sąrašą
        while len(q_list) < 4:
            # nustatome radio buttons ypatybes
            radio_btn = Radiobutton(langas, text=" ", variable = self.pasirinktas_ats,
            value = len(q_list) + 1, font = ("ariel", 14))
            # pridedame radio mygtuką į sąrašą
            q_list.append(radio_btn)
            # nustatome radio mygtukų vietą lange
            radio_btn.place(x = 70, y = y_pos)
            # padidinam 30 y-axis poziciją
            y_pos += 30
        # grąžinam radio mygtukus
        return q_list



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