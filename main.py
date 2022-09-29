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



langas = tk.Tk()
langas.title("Shuffle Music")
programa = PagrindinisLangas(langas)
langas.mainloop()