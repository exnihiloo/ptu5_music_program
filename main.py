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
        self.random_queen = ['https://music.youtube.com/watch?v=yl3TsqL0ZPw',
                    'https://music.youtube.com/watch?v=3O0D6MvWFf4',
                    'https://music.youtube.com/watch?v=CczcMarUoVk',
                    'https://music.youtube.com/watch?v=RJo21ubguDE',
                    'https://music.youtube.com/watch?v=lXPftnU63mQ',
                    'https://music.youtube.com/watch?v=x8hUwP_5Qc4',
                    'https://music.youtube.com/watch?v=wIqa9uVnXCQ',
                    'https://music.youtube.com/watch?v=bR-gZQLO26w',
                    'https://music.youtube.com/watch?v=91BmiDSbUwU',
                    'https://music.youtube.com/watch?v=-tJYN-eG1zk'
                    ]
        webbrowser.open(choice(self.random_queen), new = 2)
        

    def open_acdc(self):
        self.random_acdc = ['https://music.youtube.com/watch?v=9vWNauaZAgg',
                            'https://music.youtube.com/watch?v=ikFFVfObwss',
                            'https://music.youtube.com/watch?v=GL56LY6fE0E',
                            'https://music.youtube.com/watch?v=NhsK5WExrnE',
                            'https://music.youtube.com/watch?v=iaaRYZPu9dc',
                            'https://music.youtube.com/watch?v=lhg9bYNLvOg',
                            'https://music.youtube.com/watch?v=waF-lPzvFUc',
                            'https://music.youtube.com/watch?v=wAfPLyLzCkQ',
                            'https://music.youtube.com/watch?v=zEv7PkfGKRA',
                            'https://music.youtube.com/watch?v=kq_GSIw0X0w'
                        ]
        webbrowser.open(choice(self.random_acdc), new = 2)

    def open_doors(self):
        self.random_doors = ['https://music.youtube.com/watch?v=vHXjcdNIN-Q',
                            'https://music.youtube.com/watch?v=lJZTgynPGT8',
                            'https://music.youtube.com/watch?v=-NyC6mrutj0',
                            'https://music.youtube.com/watch?v=rtU0ss9Zki4',
                            'https://music.youtube.com/watch?v=dV0buYqrRo4',
                            'https://music.youtube.com/watch?v=BXqPNlng6uI',
                            'https://music.youtube.com/watch?v=VUI-ELCdjxo',
                            'https://music.youtube.com/watch?v=jKU74Uns9_0',
                            'https://music.youtube.com/watch?v=nbtEkZIvMAg',
                            'https://music.youtube.com/watch?v=AVez4RS7IJw'
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