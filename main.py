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


class VidinisReggae:
    def __init__(self, master):
        self.master = master
        self.bobm = tk.Button(self.master, text = "Bob Marley", width = 15, command = self.open_bobm)
        self.bobm.pack()




langas = tk.Tk()
langas.title("Shuffle Music")
programa = PagrindinisLangas(langas)
langas.mainloop()