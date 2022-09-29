from tkinter import *
import tkinter as tk
import webbrowser
from random import choice

class PagrindinisLangas:
    def __init__(self, master):
        self.master = master
        self.rock_langas = tk.Button(self.master, text = "\U0001F918 Rock", width = 15, command = self.new_window)
        self.reggae_langas = tk.Button(self.master, text = "\u262E Reggae", width = 15, command = self.new_window2)
        self.rock_langas.pack()
        self.reggae_langas.pack()

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.app = VidinisRock(self.vidinis)

    def new_window2(self):
        self.vidinis2 = tk.Toplevel(self.master)
        self.app = VidinisReggae(self.vidinis2)


class VidinisRock:
    def __init__(self, master):
        self.master = master
        self.queen = tk.Button(self.master, text = "Queen", width = 15, command = self.open_qeen)
        self.acdc = tk.Button(self.master, text = "AC/DC", width = 15, command = self.open_acdc)
        self.doors = tk.Button(self.master, text = "The Doors", width = 15, command = self.open_doors)
        self.queen.pack()
        self.acdc.pack()
        self.doors.pack()

    def open_qeen(self):
        self.random_queen = ['https://www.youtube.com/watch?v=ro9QAtTnihc&list=PLqIK01W9QdPmZoPyEmIDrnT23J4NGloCh&index=4',
                    'https://www.youtube.com/watch?v=Nzas1p0BqWc&list=PLqIK01W9QdPmZoPyEmIDrnT23J4NGloCh&index=5',
                    'https://www.youtube.com/watch?v=yl3TsqL0ZPw&list=PLqIK01W9QdPmZoPyEmIDrnT23J4NGloCh&index=7',
                    'https://www.youtube.com/watch?v=2CW9Pd3W15I&list=PLqIK01W9QdPmZoPyEmIDrnT23J4NGloCh&index=10',
                    'https://www.youtube.com/watch?v=ja8lWt5Dvk4&list=PLqIK01W9QdPmZoPyEmIDrnT23J4NGloCh&index=11'
                    ]
        webbrowser.open(choice(self.random_queen), new = 2)
        

    def open_acdc(self):
        self.random_acdc = ['https://www.youtube.com/watch?v=v2AC41dglnM',
                            'https://www.youtube.com/watch?v=gEPmA3USJdI',
                            'https://www.youtube.com/watch?v=pAgnJDJN4VA',
                            'https://www.youtube.com/watch?v=Lo2qQmj0_h4',
                            'https://www.youtube.com/watch?v=wLoWd2KyUro'
                        ]
        webbrowser.open(choice(self.random_acdc), new = 2)

    def open_doors(self):
        self.random_doors = ['https://www.youtube.com/watch?v=iv8GW1GaoIc',
                            'https://www.youtube.com/watch?v=mbj1RFaoyLk',
                            'https://www.youtube.com/watch?v=PAK5blgfKWM',
                            'https://www.youtube.com/watch?v=IsbIXm30c8k',
                            'https://www.youtube.com/watch?v=NFeUko-lQHg',
                            'https://www.youtube.com/watch?v=-NyC6mrutj0'
                        ]
        webbrowser.open(choice(self.random_doors), new = 2)

class VidinisReggae:
    def __init__(self, master):
        self.master = master
        self.bobm = tk.Button(self.master, text = "Bob Marley", width = 15, command = self.open_bobm)
        self.bobm.pack()

    def open_bobm(self):
        self.random_bobm = ['https://www.youtube.com/watch?v=5M0NqIRglGA',
                            'https://www.youtube.com/watch?v=69RdQFDuYPI',
                            'https://www.youtube.com/watch?v=1Ogjp1hzmZU',
                            'https://www.youtube.com/watch?v=hRd2dSdIvbU',
                            'https://www.youtube.com/watch?v=jJzJewlOfVs'
                        ]
        webbrowser.open(choice(self.random_bobm), new = 2)



langas = tk.Tk()
langas.title("Shuffle Music")
programa = PagrindinisLangas(langas)
langas.mainloop()