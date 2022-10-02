from tkinter import *
import tkinter as tk
import webbrowser
from random import choice
from tkinter import ttk

class PagrindinisLangas:
    def __init__(self, master):
        self.master = master
        self.uzrasas = Label(self.master, text = 'Išsirinkite muzikos žanrą', font = ('Courier New', 20, "bold"), fg = 'white', bg = 'black')
        self.uzrasas.pack(pady = 50)
        self.rock_langas = tk.Button(self.master, text = "\U0001F918 Rock", width = 15, command = self.new_window, highlightbackground='black')
        self.reggae_langas = tk.Button(self.master, text = "\u262E Reggae", width = 15, command = self.new_window2, highlightbackground='black')
        self.hmetal_langas = tk.Button(self.master, text = "\U0001F3B8 Heavy Metal", width = 15, command = self.new_window3, highlightbackground='black')
        self.punk_langas = tk.Button(self.master, text = "\U0001F577 Punk", width = 15, command = self.new_window4, highlightbackground='black')
        self.black_metal_langas = tk.Button(self.master, text = "\U0001F480 Black Metal", width = 15, command = self.new_window5, highlightbackground='black')
        self.rap_langas = tk.Button(self.master, text = "\U0001F576 Rap", width = 15, command = self.new_window6, highlightbackground='black')
        self.pop_langas = tk.Button(self.master, text = "\U0001F46F Pop", width = 15, command = self.new_window7, highlightbackground='black')
        self.disco_langas = tk.Button(self.master, text = "\U0001F4BF Disco", width = 15, command = self.new_window8, highlightbackground='black')
        self.jazz_langas = tk.Button(self.master, text = "\U0001F3B7 Jazz", width = 15, command = self.new_window9, highlightbackground='black')
        self.blues_langas = tk.Button(self.master, text = "\U0001FA95 Blues", width = 15, command = self.new_window10, highlightbackground='black')
        self.uzdaryti_main = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground='black')
        self.rock_langas.pack()
        self.reggae_langas.pack()
        self.hmetal_langas.pack()
        self.punk_langas.pack()
        self.black_metal_langas.pack()
        self.rap_langas.pack()
        self.pop_langas.pack()
        self.disco_langas.pack()
        self.jazz_langas.pack()
        self.blues_langas.pack()
        self.uzdaryti_main.pack()

    def uzdaryti(self):
        self.master.quit()

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.vidinis.title("\U0001F918 Rock")
        self.vidinis.configure(bg = "red")
        self.vidinis.geometry("410x350")
        self.app = VidinisRock(self.vidinis)

    def new_window2(self):
        self.vidinis2 = tk.Toplevel(self.master)
        self.vidinis2.title("\u262E Reggae")
        self.vidinis2.configure(bg = "green")
        self.vidinis2.geometry("410x350")
        self.app = VidinisReggae(self.vidinis2)

    def new_window3(self):
        self.vidinis3 = tk.Toplevel(self.master)
        self.vidinis3.title("\U0001F3B8 Heavy Metal")
        self.vidinis3.configure(bg = "grey")
        self.vidinis3.geometry("410x350")
        self.app = VidinisHeavyMetal(self.vidinis3)
    
    def new_window4(self):
        self.vidinis4 = tk.Toplevel(self.master)
        self.vidinis4.title("\U0001F577 Punk")
        self.vidinis4.configure(bg = "MediumPurple4")
        self.vidinis4.geometry("410x350")
        self.app = VidinisPunk(self.vidinis4)

    def new_window5(self):
        self.vidinis5 = tk.Toplevel(self.master)
        self.vidinis5.title("\U0001F480 Black Metal")
        self.vidinis5.configure(bg = "midnight blue")
        self.vidinis5.geometry("410x350")
        self.app = VidinisBlackMetal(self.vidinis5)

    def new_window6(self):
        self.vidinis6 = tk.Toplevel(self.master)
        self.vidinis6.title("\U0001F576 Rap")
        self.vidinis6.configure(bg = "IndianRed4")
        self.vidinis6.geometry("410x350")
        self.app = VidinisRap(self.vidinis6)

    def new_window7(self):
        self.vidinis7 = tk.Toplevel(self.master)
        self.vidinis7.title("\U0001F46F Pop")
        self.vidinis7.configure(bg = "hot pink")
        self.vidinis7.geometry("410x350")
        self.app = VidinisPop(self.vidinis7)

    def new_window8(self):
        self.vidinis8 = tk.Toplevel(self.master)
        self.vidinis8.title("\U0001F4BF Disco")
        self.vidinis8.configure(bg = "cyan")
        self.vidinis8.geometry("410x350")
        self.app = VidinisDisco(self.vidinis8)

    def new_window9(self):
        self.vidinis9 = tk.Toplevel(self.master)
        self.vidinis9.title("\U0001F3B7 Jazz")
        self.vidinis9.configure(bg = "DarkGoldenrod1")
        self.vidinis9.geometry("410x350")
        self.app = VidinisJazz(self.vidinis9)

    def new_window10(self):
        self.vidinis10 = tk.Toplevel(self.master)
        self.vidinis10.title("\U0001FA95 Blues")
        self.vidinis10.configure(bg = "burlywood4")
        self.vidinis10.geometry("410x350")
        self.app = VidinisBlues(self.vidinis10)

class VidinisRock:
    def __init__(self, master):
        self.master = master
        self.queen = tk.Button(self.master, text = "Queen", width = 15, command = self.open_qeen, highlightbackground='red')
        self.acdc = tk.Button(self.master, text = "AC/DC", width = 15, command = self.open_acdc, highlightbackground='red')
        self.doors = tk.Button(self.master, text = "The Doors", width = 15, command = self.open_doors, highlightbackground='red')
        self.ledzep = tk.Button(self.master, text = "Led Zeppelin", width = 15, command = self.open_ledzep, highlightbackground='red')
        self.deep_purple = tk.Button(self.master, text = "Deep Purple", width = 15, command = self.open_deep_purple, highlightbackground='red')
        self.uzdarytirock = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='red')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "red")
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "red")
       # kuriam atlikėjų ir jų dainų sąrašus
        self.atlikeju_sarasas = ['Queen', "AC/DC", "The Doors", "Led Zeppelin", "Deep Purple"]
        self.queen_dainos = ["Bohemian Rhapsody", 
                            "The Show Must Go On", 
                            "Dont Stop Me Now", 
                            "I want It All",
                            "Scandal", 
                            "Somebody to Love", 
                            "I Want to Break Free", 
                            "Killer Queen",
                            "Love of My Life",
                            "We Will Rock You"
                        ]
        self.acdc_dainos = ["Back in Black", 
                            "Highway to Hell", 
                            "Hells Bells", 
                            "T.N.T", 
                            "Moneytalks", 
                            "Thunderstruck",
                            "Rock or Bust", 
                            "Stiff Upper Lip", 
                            "Are You Ready", 
                            "The Jack"
                        ]
        self.doors_dainos = ["L.A. Woman",
                            "Riders on the Storm",
                            "People are Strange",
                            "Roadhouse Blues",
                            "Crawling King Snake",
                            "The End",
                            "Waiting for the Sun",
                            "Light My Fire",
                            "Alabama Song (Whiskey Bar)",
                            "Love Me Two Times"
                        ]
        self.led_zep_dainos = ["Stairway to Heaven",
                            "Whole Lotta Love",
                            "Kashmir",
                            "Dazed and Confused",
                            "Immigrant Song",
                            "Black Dog",
                            "Baby I'm Gonna Leave You",
                            "Rock and Roll",
                            "The Rain Song",
                            "Communication Breakdown"
                        ]
        self.deep_purple_dainos = ["Smoke on the Water",
                                "Perfect Strangers",
                                "Child in Time",
                                "Highway Star",
                                "Black Night",
                                "Call of the Wild",
                                "Space Truckin'",
                                "Speed King",
                                "Burn",
                                "Hush"
                            ]

        # kuriam atlikėjų dropdown box
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 9, column=0)
        # bindinam boksą
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)

        # kuriam kitą boksą
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 9, column = 1)

        # pasirinkimo mygtukas
        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='red', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 10, columnspan=2)
       
        self.uzrasas1.grid(row = 0, columnspan=2)
        self.queen.grid(row = 1, columnspan=2)
        self.acdc.grid(row = 2, columnspan=2)
        self.doors.grid(row = 3, columnspan=2)
        self.ledzep.grid(row = 4, columnspan=2)
        self.deep_purple.grid(row = 5, columnspan=2)
        self.uzdarytirock.grid(row = 15, columnspan=2)
        self.uzrasas2.grid(row = 8, columnspan=2)

    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Queen":
            self.dainu_boks.config(value = self.queen_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "AC/DC":
            self.dainu_boks.config(value = self.acdc_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "The Doors":
            self.dainu_boks.config(value = self.doors_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Led Zeppelin":
            self.dainu_boks.config(value = self.led_zep_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Deep Purple":
            self.dainu_boks.config(value = self.deep_purple_dainos)
            self.dainu_boks.current(0)

    def picker(self):
        if self.dainu_boks.get() == "Bohemian Rhapsody":
            webbrowser.open(('https://music.youtube.com/watch?v=yl3TsqL0ZPw'), new = 2)
        if self.dainu_boks.get() == "The Show Must Go On":
            webbrowser.open(('https://music.youtube.com/watch?v=3O0D6MvWFf4'), new = 2)
        if self.dainu_boks.get() == "Dont Stop Me Now":
            webbrowser.open(('https://music.youtube.com/watch?v=CczcMarUoVk'), new = 2)
        if self.dainu_boks.get() == "I want It All":
            webbrowser.open(('https://music.youtube.com/watch?v=RJo21ubguDE'), new = 2)
        if self.dainu_boks.get() == "Scandal":
            webbrowser.open(('https://music.youtube.com/watch?v=lXPftnU63mQ'), new = 2)
        if self.dainu_boks.get() == "Somebody to Love":
            webbrowser.open(('https://music.youtube.com/watch?v=x8hUwP_5Qc4'), new = 2)
        if self.dainu_boks.get() == "I Want to Break Free":
            webbrowser.open(('https://music.youtube.com/watch?v=wIqa9uVnXCQ'), new = 2)
        if self.dainu_boks.get() == "Killer Queen":
            webbrowser.open(('https://music.youtube.com/watch?v=bR-gZQLO26w'), new = 2)
        if self.dainu_boks.get() == "Love of My Life":
            webbrowser.open(('https://music.youtube.com/watch?v=91BmiDSbUwU'), new = 2)
        if self.dainu_boks.get() == "We Will Rock You":
            webbrowser.open(('https://music.youtube.com/watch?v=-tJYN-eG1zk'), new = 2)
        if self.dainu_boks.get() == "Back in Black":
            webbrowser.open(('https://music.youtube.com/watch?v=9vWNauaZAgg'), new = 2)
        if self.dainu_boks.get() == "Highway to Hell":
            webbrowser.open(('https://music.youtube.com/watch?v=ikFFVfObwss'), new = 2)
        if self.dainu_boks.get() == "Hells Bells":
            webbrowser.open(('https://music.youtube.com/watch?v=GL56LY6fE0E'), new = 2)
        if self.dainu_boks.get() == "T.N.T":
            webbrowser.open(('https://music.youtube.com/watch?v=NhsK5WExrnE'), new = 2)
        if self.dainu_boks.get() == "Moneytalks":
            webbrowser.open(('https://music.youtube.com/watch?v=iaaRYZPu9dc'), new = 2)
        if self.dainu_boks.get() == "Thunderstruck":
            webbrowser.open(('https://music.youtube.com/watch?v=lhg9bYNLvOg'), new = 2)
        if self.dainu_boks.get() == "Rock or Bust":
            webbrowser.open(('https://music.youtube.com/watch?v=waF-lPzvFUc'), new = 2)
        if self.dainu_boks.get() == "Stiff Upper Lip":
            webbrowser.open(('https://music.youtube.com/watch?v=wAfPLyLzCkQ'), new = 2)
        if self.dainu_boks.get() == "Are You Ready":
            webbrowser.open(('https://music.youtube.com/watch?v=zEv7PkfGKRA'), new = 2)
        if self.dainu_boks.get() == "The Jack":
            webbrowser.open(('https://music.youtube.com/watch?v=kq_GSIw0X0w'), new = 2)
        if self.dainu_boks.get() == "L.A. Woman":
            webbrowser.open(('https://music.youtube.com/watch?v=vHXjcdNIN-Q'), new = 2)
        if self.dainu_boks.get() == "Riders on the Storm":
            webbrowser.open(('https://music.youtube.com/watch?v=lJZTgynPGT8'), new = 2)
        if self.dainu_boks.get() == "People are Strange":
            webbrowser.open(('https://music.youtube.com/watch?v=-NyC6mrutj0'), new = 2)
        if self.dainu_boks.get() == "Roadhouse Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=rtU0ss9Zki4'), new = 2)
        if self.dainu_boks.get() == "Crawling King Snake":
            webbrowser.open(('https://music.youtube.com/watch?v=dV0buYqrRo4'), new = 2)
        if self.dainu_boks.get() == "The End":
            webbrowser.open(('https://music.youtube.com/watch?v=BXqPNlng6uI'), new = 2)
        if self.dainu_boks.get() == "Waiting for the Sun":
            webbrowser.open(('https://music.youtube.com/watch?v=VUI-ELCdjxo'), new = 2)
        if self.dainu_boks.get() == "Light My Fire":
            webbrowser.open(('https://music.youtube.com/watch?v=jKU74Uns9_0'), new = 2)
        if self.dainu_boks.get() == "Alabama Song (Whiskey Bar)":
            webbrowser.open(('https://music.youtube.com/watch?v=nbtEkZIvMAg'), new = 2)
        if self.dainu_boks.get() == "Love Me Two Times":
            webbrowser.open(('https://music.youtube.com/watch?v=AVez4RS7IJw'), new = 2)
        if self.dainu_boks.get() == "Stairway to Heaven":
            webbrowser.open(('https://music.youtube.com/watch?v=X791IzOwt3Q'), new = 2)
        if self.dainu_boks.get() == "Whole Lotta Love":
            webbrowser.open(('https://music.youtube.com/watch?v=0bcIjILqORM'), new = 2)
        if self.dainu_boks.get() == "Kashmir":
            webbrowser.open(('https://music.youtube.com/watch?v=tzVJPgCn-Z8'), new = 2)
        if self.dainu_boks.get() == "Dazed and Confused":
            webbrowser.open(('https://music.youtube.com/watch?v=yO2n7QoyieM'), new = 2)
        if self.dainu_boks.get() == "Immigrant Song":
            webbrowser.open(('https://music.youtube.com/watch?v=5eHkjPCGXKQ'), new = 2)
        if self.dainu_boks.get() == "Black Dog":
            webbrowser.open(('https://music.youtube.com/watch?v=yBuub4Xe1mw'), new = 2)
        if self.dainu_boks.get() == "Baby I'm Gonna Leave You":
            webbrowser.open(('https://music.youtube.com/watch?v=UyOg0mt2R2k'), new = 2)
        if self.dainu_boks.get() == "Rock and Roll":
            webbrowser.open(('https://music.youtube.com/watch?v=RCN6eRVav5k'), new = 2)
        if self.dainu_boks.get() == "The Rain Song":
            webbrowser.open(('https://music.youtube.com/watch?v=TRt4hQs3nH0'), new = 2)
        if self.dainu_boks.get() == "Communication Breakdown":
            webbrowser.open(('https://music.youtube.com/watch?v=3EH7QMVnSRI'), new = 2)
        if self.dainu_boks.get() == "Smoke on the Water":
            webbrowser.open(('https://music.youtube.com/watch?v=1L3XxUxEb6U'), new = 2)
        if self.dainu_boks.get() == "Perfect Strangers":
            webbrowser.open(('https://music.youtube.com/watch?v=z6Y4_jigI-4'), new = 2)
        if self.dainu_boks.get() == "Child in Time":
            webbrowser.open(('https://music.youtube.com/watch?v=ybQnFhTr2I8'), new = 2)
        if self.dainu_boks.get() == "Highway Star":
            webbrowser.open(('https://music.youtube.com/watch?v=_hJEyDOn6Ho'), new = 2)
        if self.dainu_boks.get() == "Black Night":
            webbrowser.open(('https://music.youtube.com/watch?v=pLLuifWR4Mg'), new = 2)
        if self.dainu_boks.get() == "Call of the Wild":
            webbrowser.open(('https://music.youtube.com/watch?v=0pxllXxQ8kw'), new = 2)
        if self.dainu_boks.get() == "Space Truckin'":
            webbrowser.open(('https://music.youtube.com/watch?v=Xt9W_tf32dQ'), new = 2)
        if self.dainu_boks.get() == "Speed King":
            webbrowser.open(('https://music.youtube.com/watch?v=W_jfHvcAXRY'), new = 2)
        if self.dainu_boks.get() == "Burn":
            webbrowser.open(('https://music.youtube.com/watch?v=jgbf03MJyS4'), new = 2)
        if self.dainu_boks.get() == "Hush":
            webbrowser.open(('https://music.youtube.com/watch?v=Y4eH033TGOo'), new = 2)

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


    def open_ledzep(self):
        self.random_ledzep = ['https://music.youtube.com/watch?v=X791IzOwt3Q',
                            'https://music.youtube.com/watch?v=0bcIjILqORM',
                            'https://music.youtube.com/watch?v=tzVJPgCn-Z8',
                            'https://music.youtube.com/watch?v=yO2n7QoyieM',
                            'https://music.youtube.com/watch?v=5eHkjPCGXKQ',
                            'https://music.youtube.com/watch?v=yBuub4Xe1mw',
                            'https://music.youtube.com/watch?v=UyOg0mt2R2k',
                            'https://music.youtube.com/watch?v=RCN6eRVav5k',
                            'https://music.youtube.com/watch?v=TRt4hQs3nH0',
                            'https://music.youtube.com/watch?v=3EH7QMVnSRI'
                        ]
        webbrowser.open(choice(self.random_ledzep), new = 2)

    def open_deep_purple(self):
        self.random_deep_purple = ['https://music.youtube.com/watch?v=1L3XxUxEb6U',
                                'https://music.youtube.com/watch?v=z6Y4_jigI-4',
                                'https://music.youtube.com/watch?v=ybQnFhTr2I8',
                                'https://music.youtube.com/watch?v=_hJEyDOn6Ho',
                                'https://music.youtube.com/watch?v=pLLuifWR4Mg',
                                'https://music.youtube.com/watch?v=0pxllXxQ8kw',
                                'https://music.youtube.com/watch?v=Xt9W_tf32dQ',
                                'https://music.youtube.com/watch?v=W_jfHvcAXRY',
                                'https://music.youtube.com/watch?v=jgbf03MJyS4',
                                'https://music.youtube.com/watch?v=Y4eH033TGOo'
                            ]
        webbrowser.open(choice(self.random_deep_purple), new = 2)

    def uzdaryti(self):
        self.master.destroy()

class VidinisReggae:
    def __init__(self, master):
        self.master = master
        self.bobm = tk.Button(self.master, text = "Bob Marley & The Wailers", width = 15, command = self.open_bobm, highlightbackground='green')
        self.peter = tk.Button(self.master, text = "Peter Tosh", width = 15, command = self.open_peter_tosh, highlightbackground='green')
        self.mouse = tk.Button(self.master, text = "Eek-A-Mouse", width = 15, command = self.open_eekmouse, highlightbackground='green')
        self.damianm = tk.Button(self.master, text = "Damian Marley", width = 15, command = self.open_damian_marley, highlightbackground='green')
        self.albarosie = tk.Button(self.master, text = "Alborosie", width = 15, command = self.open_albarosie, highlightbackground='green')
        self.uzdarytireggae = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='green')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "green")
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "green")
        self.atlikeju_sarasas = ["Bob Marley & The Wailers", "Peter Tosh", "Eek-A-Mouse", "Damian Marley", "Alborosie"]
        self.bobm_dainos = ["Redemption Song",
                            "Three Little Birds",
                            "Could You Be Loved",
                            "Is this Love",
                            "Waiting in Vain",
                            "Zion Train",
                            "Buffalo Soldier",
                            "Stir It Up",
                            "Shot the Sheriff",
                            "No Woman No Cry"
                        ]
        self.peter_dainos = ["Legalize It",
                            "I am That I Am",
                            "The Poor Man Feel It",
                            "Not Gonna Give It Up",
                            "Pick Myself Up",
                            "Glass House",
                            "Stepping Razor",
                            "Wanted Dead or Alive",
                            "Bush Doctor",
                            "Till Your Well Runs Dry"
                        ]

        self.eekmouse_dainos = ["Mr. Government",
                                "Wa-Do-Dem",
                                "Ganja Smuggling",
                                "Rude Boy Jamaican",
                                "Border Patrol",
                                "No Wicked Can't Reign",
                                "Controversial Song",
                                "Lonesome Journey",
                                "My Father's Land",
                                "Glamity"
                            ]
        self.damianm_dainos = ["Medication",
                            "Welcome to Jamrock",
                            "Road to Zion",
                            "Patience",
                            "There For You",
                            "Speak Life",
                            "Living It Up",
                            "Friends",
                            "Move!",
                            "Set Up Shop"
                        ]
        self.dainos_alborosie = ["Kingston Town",
                                "Herbalist",
                                "No Cocaine",
                                "Still Blazing",
                                "Rastafari Anthem",
                                "Who You Think You Are",
                                "Cry",
                                "Hustlers Never Sleep",
                                "Real Story",
                                "Diversity"
                            ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column = 0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkta_daina)

        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column = 1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='green', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan=2)

        self.uzrasas1.grid(row = 0, columnspan=2)
        self.bobm.grid(row = 1, columnspan=2)
        self.peter.grid(row = 2, columnspan=2)
        self.mouse.grid(row = 3, columnspan=2)
        self.damianm.grid(row = 4, columnspan=2)
        self.albarosie.grid(row = 5, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        self.uzdarytireggae.grid(row = 12, columnspan=2)


    def picker(self):
        if self.dainu_boks.get() == "Redemption Song":
            webbrowser.open(('https://music.youtube.com/watch?v=1A95dcLxAuA'), new = 2)
        if self.dainu_boks.get() == "Three Little Birds":
            webbrowser.open(('https://music.youtube.com/watch?v=MUNNRAdizz0'), new = 2)
        if self.dainu_boks.get() == "Could You Be Loved":
            webbrowser.open(('https://music.youtube.com/watch?v=zBqW6yKz8WA'), new = 2)
        if self.dainu_boks.get() == "Is this Love":
            webbrowser.open(('https://music.youtube.com/watch?v=co2FK0WbXX0'), new = 2)
        if self.dainu_boks.get() == "Waiting in Vain":
            webbrowser.open(('https://music.youtube.com/watch?v=TBq4_pk_W24'), new = 2)
        if self.dainu_boks.get() == "Zion Train":
            webbrowser.open(('https://music.youtube.com/watch?v=SfKJKn8srCY'), new = 2)
        if self.dainu_boks.get() == "Buffalo Soldier":
            webbrowser.open(('https://music.youtube.com/watch?v=dBWTZF38Hxc'), new = 2)
        if self.dainu_boks.get() == "Stir It Up":
            webbrowser.open(('https://music.youtube.com/watch?v=nFQ--eDfwL0'), new = 2)
        if self.dainu_boks.get() == "Shot the Sheriff":
            webbrowser.open(('https://music.youtube.com/watch?v=tvBfolZUn9o'), new = 2)
        if self.dainu_boks.get() == "No Woman No Cry":
            webbrowser.open(('https://music.youtube.com/watch?v=ACIYuW91Zms'), new = 2)
        if self.dainu_boks.get() == "Legalize It":
            webbrowser.open(('https://music.youtube.com/watch?v=5TKIqU1AfNk'), new = 2)
        if self.dainu_boks.get() == "I am That I Am":
            webbrowser.open(('https://music.youtube.com/watch?v=CqgaPR8p6fA'), new = 2)
        if self.dainu_boks.get() == "The Poor Man Feel It":
            webbrowser.open(('https://music.youtube.com/watch?v=Xmqt6zRQKR4'), new = 2)
        if self.dainu_boks.get() == "Not Gonna Give It Up":
            webbrowser.open(('https://music.youtube.com/watch?v=NOgFvBZgogg'), new = 2)
        if self.dainu_boks.get() == "Pick Myself Up":
            webbrowser.open(('https://music.youtube.com/watch?v=4yOXLBIh8ok'), new = 2)
        if self.dainu_boks.get() == "Glass House":
            webbrowser.open(('https://music.youtube.com/watch?v=p2JDJ31aFMs'), new = 2)
        if self.dainu_boks.get() == "Stepping Razor":
            webbrowser.open(('https://music.youtube.com/watch?v=5WZY1cEecbI'), new = 2)
        if self.dainu_boks.get() == "Wanted Dead or Alive":
            webbrowser.open(('https://music.youtube.com/watch?v=h87cbH7Iogc'), new = 2)
        if self.dainu_boks.get() == "Bush Doctor":
            webbrowser.open(('https://music.youtube.com/watch?v=yzTz0sCtkCQ'), new = 2)
        if self.dainu_boks.get() == "Till Your Well Runs Dry":
            webbrowser.open(('https://music.youtube.com/watch?v=oY8CJiz9Ug4'), new = 2)
        if self.dainu_boks.get() == "Mr. Government":
            webbrowser.open(('https://music.youtube.com/watch?v=EL2LXSAQrqg'), new = 2)
        if self.dainu_boks.get() == "Wa-Do-Dem":
            webbrowser.open(('https://music.youtube.com/watch?v=pBFPgVID0Go'), new = 2)
        if self.dainu_boks.get() == "Ganja Smuggling":
            webbrowser.open(('https://music.youtube.com/watch?v=Svekpf56P0c'), new = 2)
        if self.dainu_boks.get() == "Rude Boy Jamaican":
            webbrowser.open(('https://music.youtube.com/watch?v=yUyTVI2r104'), new = 2)
        if self.dainu_boks.get() == "Border Patrol":
            webbrowser.open(('https://music.youtube.com/watch?v=4wf7NqrO-Fo'), new = 2)
        if self.dainu_boks.get() == "No Wicked Can't Reign":
            webbrowser.open(('https://music.youtube.com/watch?v=Qb4Pcod9bpk'), new = 2)
        if self.dainu_boks.get() == "Controversial Song":
            webbrowser.open(('https://music.youtube.com/watch?v=Yco8vyMjjfs'), new = 2)
        if self.dainu_boks.get() == "Lonesome Journey":
            webbrowser.open(('https://music.youtube.com/watch?v=63B6iskZmF8'), new = 2)
        if self.dainu_boks.get() == "My Father's Land":
            webbrowser.open(('https://music.youtube.com/watch?v=kr_cPdLVBQg'), new = 2)
        if self.dainu_boks.get() == "Glamity":
            webbrowser.open(('https://music.youtube.com/watch?v=yO7d0iELipc'), new = 2)
        if self.dainu_boks.get() == "Medication":
            webbrowser.open(('https://music.youtube.com/watch?v=lF7jYuwqbik'), new = 2)
        if self.dainu_boks.get() == "Welcome to Jamrock":
            webbrowser.open(('https://music.youtube.com/watch?v=UmRmikGECjw'), new = 2)
        if self.dainu_boks.get() == "Road to Zion":
            webbrowser.open(('https://music.youtube.com/watch?v=uDsJB_zUquo'), new = 2)
        if self.dainu_boks.get() == "Patience":
            webbrowser.open(('https://music.youtube.com/watch?v=y4NlW43QNQQ'), new = 2)
        if self.dainu_boks.get() == "There For You":
            webbrowser.open(('https://music.youtube.com/watch?v=E8qgqTf9bZQ'), new = 2)
        if self.dainu_boks.get() == "Speak Life":
            webbrowser.open(('https://music.youtube.com/watch?v=sQRJnU1LR2A'), new = 2)
        if self.dainu_boks.get() == "Living It Up":
            webbrowser.open(('https://music.youtube.com/watch?v=sQpC15NICSg'), new = 2)
        if self.dainu_boks.get() == "Friends":
            webbrowser.open(('https://music.youtube.com/watch?v=e2d-LfagPRk'), new = 2)
        if self.dainu_boks.get() == "Move!":
            webbrowser.open(('https://music.youtube.com/watch?v=eiAIo0l1F9I'), new = 2)
        if self.dainu_boks.get() == "Set Up Shop":
            webbrowser.open(('https://music.youtube.com/watch?v=1ML2w6BZv8s'), new = 2)
        if self.dainu_boks.get() == "Kingston Town":
            webbrowser.open(('https://music.youtube.com/watch?v=AmbN5CSDn8U'), new = 2)
        if self.dainu_boks.get() == "Herbalist":
            webbrowser.open(('https://music.youtube.com/watch?v=buVpkh39Cv0'), new = 2)
        if self.dainu_boks.get() == "No Cocaine":
            webbrowser.open(('https://music.youtube.com/watch?v=rFwRfb_MReY'), new = 2)
        if self.dainu_boks.get() == "Still Blazing":
            webbrowser.open(('https://music.youtube.com/watch?v=2hNrpccMV08'), new = 2)
        if self.dainu_boks.get() == "Rastafari Anthem":
            webbrowser.open(('https://music.youtube.com/watch?v=5sa3XroriNY'), new = 2)
        if self.dainu_boks.get() == "Who You Think You Are":
            webbrowser.open(('https://music.youtube.com/watch?v=K6o1ihu1NKw'), new = 2)
        if self.dainu_boks.get() == "Cry":
            webbrowser.open(('https://music.youtube.com/watch?v=8tDLossnSkQ'), new = 2)
        if self.dainu_boks.get() == "Hustlers Never Sleep":
            webbrowser.open(('https://music.youtube.com/watch?v=lAzJN3i62aI'), new = 2)
        if self.dainu_boks.get() == "Real Story":
            webbrowser.open(('https://music.youtube.com/watch?v=oHthj_oULRc'), new = 2)
        if self.dainu_boks.get() == "Diversity":
            webbrowser.open(('https://music.youtube.com/watch?v=VlX0b_axejQ'), new = 2)
        

    def pasirinkta_daina(self, value):
        if self.atlikeju_boks.get() == "Bob Marley & The Wailers":
            self.dainu_boks.config(value = self.bobm_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Peter Tosh":
            self.dainu_boks.config(value = self.peter_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Eek-A-Mouse":
            self.dainu_boks.config(value = self.eekmouse_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Damian Marley":
            self.dainu_boks.config(value = self.damianm_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Alborosie":
            self.dainu_boks.config(value = self.dainos_alborosie)
            self.dainu_boks.current(0)

    def open_bobm(self):
        self.random_bobm = ['https://music.youtube.com/watch?v=1A95dcLxAuA',
                            'https://music.youtube.com/watch?v=MUNNRAdizz0',
                            'https://music.youtube.com/watch?v=zBqW6yKz8WA',
                            'https://music.youtube.com/watch?v=co2FK0WbXX0',
                            'https://music.youtube.com/watch?v=TBq4_pk_W24',
                            'https://music.youtube.com/watch?v=SfKJKn8srCY',
                            'https://music.youtube.com/watch?v=dBWTZF38Hxc',
                            'https://music.youtube.com/watch?v=nFQ--eDfwL0',
                            'https://music.youtube.com/watch?v=tvBfolZUn9o',
                            'https://music.youtube.com/watch?v=ACIYuW91Zms'
                        ]
        webbrowser.open(choice(self.random_bobm), new = 2)

    def open_peter_tosh(self):
        self.random_peter_tosh = ['https://music.youtube.com/watch?v=5TKIqU1AfNk',
                                'https://music.youtube.com/watch?v=CqgaPR8p6fA',
                                'https://music.youtube.com/watch?v=Xmqt6zRQKR4',
                                'https://music.youtube.com/watch?v=NOgFvBZgogg',
                                'https://music.youtube.com/watch?v=4yOXLBIh8ok',
                                'https://music.youtube.com/watch?v=p2JDJ31aFMs',
                                'https://music.youtube.com/watch?v=5WZY1cEecbI',
                                'https://music.youtube.com/watch?v=h87cbH7Iogc',
                                'https://music.youtube.com/watch?v=yzTz0sCtkCQ',
                                'https://music.youtube.com/watch?v=oY8CJiz9Ug4'
                            ]
        webbrowser.open(choice(self.random_peter_tosh), new = 2)

    def open_eekmouse(self):
        self.random_eekmouse = ['https://music.youtube.com/watch?v=EL2LXSAQrqg',
                                'https://music.youtube.com/watch?v=pBFPgVID0Go',
                                'https://music.youtube.com/watch?v=Svekpf56P0c',
                                'https://music.youtube.com/watch?v=yUyTVI2r104',
                                'https://music.youtube.com/watch?v=4wf7NqrO-Fo',
                                'https://music.youtube.com/watch?v=Qb4Pcod9bpk',
                                'https://music.youtube.com/watch?v=Yco8vyMjjfs',
                                'https://music.youtube.com/watch?v=63B6iskZmF8',
                                'https://music.youtube.com/watch?v=kr_cPdLVBQg',
                                'https://music.youtube.com/watch?v=yO7d0iELipc'
                            ]
        webbrowser.open(choice(self.random_eekmouse), new = 2)

    def open_damian_marley(self):
        self.random_damian_marley = ['https://music.youtube.com/watch?v=lF7jYuwqbik',
                                    'https://music.youtube.com/watch?v=UmRmikGECjw',
                                    'https://music.youtube.com/watch?v=uDsJB_zUquo',
                                    'https://music.youtube.com/watch?v=y4NlW43QNQQ',
                                    'https://music.youtube.com/watch?v=E8qgqTf9bZQ',
                                    'https://music.youtube.com/watch?v=sQRJnU1LR2A',
                                    'https://music.youtube.com/watch?v=sQpC15NICSg',
                                    'https://music.youtube.com/watch?v=e2d-LfagPRk',
                                    'https://music.youtube.com/watch?v=eiAIo0l1F9I',
                                    'https://music.youtube.com/watch?v=1ML2w6BZv8s'
                                ]
        webbrowser.open(choice(self.random_damian_marley), new = 2)

    def open_albarosie(self):
        self.random_albarosie = ['https://music.youtube.com/watch?v=AmbN5CSDn8U',
                                'https://music.youtube.com/watch?v=buVpkh39Cv0',
                                'https://music.youtube.com/watch?v=rFwRfb_MReY',
                                'https://music.youtube.com/watch?v=2hNrpccMV08',
                                'https://music.youtube.com/watch?v=5sa3XroriNY',
                                'https://music.youtube.com/watch?v=K6o1ihu1NKw',
                                'https://music.youtube.com/watch?v=8tDLossnSkQ',
                                'https://music.youtube.com/watch?v=lAzJN3i62aI',
                                'https://music.youtube.com/watch?v=oHthj_oULRc',
                                'https://music.youtube.com/watch?v=VlX0b_axejQ'
                            ]
        webbrowser.open(choice(self.random_albarosie), new = 2)

    def uzdaryti(self):
        self.master.destroy()

class VidinisHeavyMetal:
    def __init__(self, master):
        self.master = master
        self.ironm = tk.Button(self.master, text = "Iron Maiden", width = 15, command = self.open_ironm, highlightbackground='grey')
        self.blacksab = tk.Button(self.master, text = "Black Sabbath", width = 15, command = self.open_black_sab, highlightbackground='grey')
        self.judasp = tk.Button(self.master, text = "Judas Priest", width = 15, command = self.open_judasp, highlightbackground='grey')
        self.dio = tk.Button(self.master, text = "Dio", width = 15, command = self.open_dio, highlightbackground='grey')
        self.saxon = tk.Button(self.master, text = "Saxon", width = 15, command = self.open_saxon, highlightbackground='grey')
        self.uzdaryti_metal = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='grey')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "grey")
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "grey")
        self.atlikeju_sarasas = ["Iron Maiden", "Black Sabbath", "Judas Priest", "Dio", "Saxon"]
        self.ironm_dainos = ["Fear of the Dark",
                            "Hallowed be thy name",
                            "Trooper",
                            "Run to the Hills",
                            "Wasted Years",
                            "Powerslave",
                            "2 Minutes till Midnight",
                            "Aces High",
                            "Brave New World",
                            "Can I Play With Madness"
                        ]
        self.blacksab_dainos = ["Paranoid",
                                "N.I.B.",
                                "Into the Void",
                                "Sabbath Bloody Sabbath",
                                "Changes",
                                "Iron Man",
                                "National Acrobat",
                                "War Pigs",
                                "God is Dead?",
                                "The Wizard"
                            ]
        self.judas_priest_dainos = ["Painkiller",
                                    "Breaking the Law",
                                    "Living After Midnight",
                                    "Night Crawler",
                                    "Turbo Lover",
                                    "You've Got Another Thing Coming",
                                    "Hell Bent for Leather",
                                    "Steeler",
                                    "Blood Red Skies",
                                    "Metal Meltdown"
                                ]
        self.dio_dainos = ["Holy Diver",
                        "Rainbow in the Dark",
                        "The Last in Line",
                        "Night People",
                        "The Eyes",
                        "Straight Through the Heart",
                        "Stand Up and Shout",
                        "Killing the Dragon",
                        "Dream Evil",
                        "Shivers"
                    ]
        self.saxon_dainos = ["The Crusader",
                            "Broken Heroes",
                            "Wheels of Steel",
                            "Power & The Glory",
                            "Just Let Me Rock",
                            "Denim and Leather",
                            "Midnight Rider",
                            "Metalhead",
                            "Set Me Free",
                            "Midas Touch"
                        ]

        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column = 0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column = 1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='grey', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan = 2)

        self.uzrasas1.grid(row = 0, columnspan=2)
        self.ironm.grid(row = 1, columnspan=2)
        self.blacksab.grid(row = 2, columnspan=2)
        self.judasp.grid(row = 3, columnspan=2)
        self.dio.grid(row = 4, columnspan=2)
        self.saxon.grid(row = 5, columnspan=2)
        self.uzdaryti_metal.grid(row = 9, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        
    def picker(self):
        if self.dainu_boks.get() == "Fear of the Dark":
            webbrowser.open(('https://music.youtube.com/watch?v=bePCRKGUwAY'), new = 2)
        if self.dainu_boks.get() == "Hallowed be thy name":
            webbrowser.open(('https://music.youtube.com/watch?v=HAQQUDbuudY'), new = 2)
        if self.dainu_boks.get() == "Trooper":
            webbrowser.open(('https://music.youtube.com/watch?v=W4DfbinBgL4'), new = 2)
        if self.dainu_boks.get() == "Run to the Hills":
            webbrowser.open(('https://music.youtube.com/watch?v=Q_XJ-7jNqws'), new = 2)
        if self.dainu_boks.get() == "Wasted Years":
            webbrowser.open(('https://music.youtube.com/watch?v=ULsr-fFVjVs'), new = 2)
        if self.dainu_boks.get() == "Powerslave":
            webbrowser.open(('https://music.youtube.com/watch?v=Mw-o_cSdqmI'), new = 2)
        if self.dainu_boks.get() == "2 Minutes till Midnight":
            webbrowser.open(('https://music.youtube.com/watch?v=YCmUqAffWS8'), new = 2)
        if self.dainu_boks.get() == "Aces High":
            webbrowser.open(('https://music.youtube.com/watch?v=oNwOA84zAcE'), new = 2)
        if self.dainu_boks.get() == "Brave New World":
            webbrowser.open(('https://music.youtube.com/watch?v=X5P_muGUJR4'), new = 2)
        if self.dainu_boks.get() == "Can I Play With Madness":
            webbrowser.open(('https://music.youtube.com/watch?v=jThfgcOqwlY'), new = 2)
        if self.dainu_boks.get() == "Paranoid":
            webbrowser.open(('https://music.youtube.com/watch?v=m7nwbJLO9qo'), new = 2)
        if self.dainu_boks.get() == "N.I.B.":
            webbrowser.open(('https://music.youtube.com/watch?v=9kgQQuPZ8K0'), new = 2)
        if self.dainu_boks.get() == "Into the Void":
            webbrowser.open(('https://music.youtube.com/watch?v=-R5XnrZn47Q'), new = 2)
        if self.dainu_boks.get() == "Sabbath Bloody Sabbath":
            webbrowser.open(('https://music.youtube.com/watch?v=cYZE4vKDqzs'), new = 2)
        if self.dainu_boks.get() == "Changes":
            webbrowser.open(('https://music.youtube.com/watch?v=_eBCxYVma1g'), new = 2)
        if self.dainu_boks.get() == "Iron Man":
            webbrowser.open(('https://music.youtube.com/watch?v=b3-QqGVt-tM'), new = 2)
        if self.dainu_boks.get() == "National Acrobat":
            webbrowser.open(('https://music.youtube.com/watch?v=VcLRrG0W9hE'), new = 2)
        if self.dainu_boks.get() == "War Pigs":
            webbrowser.open(('https://music.youtube.com/watch?v=f-e8-DUqt0I'), new = 2)
        if self.dainu_boks.get() == "God is Dead?":
            webbrowser.open(('https://music.youtube.com/watch?v=kkcHZQ_hZWk'), new = 2)
        if self.dainu_boks.get() == "The Wizard":
            webbrowser.open(('https://music.youtube.com/watch?v=0BXG1zvBWKo'), new = 2)
        if self.dainu_boks.get() == "Painkiller":
            webbrowser.open(('https://music.youtube.com/watch?v=4s1gBIVOTtk'), new = 2)
        if self.dainu_boks.get() == "Breaking the Law":
            webbrowser.open(('https://music.youtube.com/watch?v=BXtPycm5dGc'), new = 2)
        if self.dainu_boks.get() == "Living After Midnight":
            webbrowser.open(('https://music.youtube.com/watch?v=PjTLOaD6fr4'), new = 2)
        if self.dainu_boks.get() == "Night Crawler":
            webbrowser.open(('https://music.youtube.com/watch?v=XUiTEob4Kzg'), new = 2)
        if self.dainu_boks.get() == "Turbo Lover":
            webbrowser.open(('https://music.youtube.com/watch?v=dp-KXWfisHA'), new = 2)
        if self.dainu_boks.get() == "You've Got Another Thing Coming":
            webbrowser.open(('https://music.youtube.com/watch?v=LNyIhirtXUI'), new = 2)
        if self.dainu_boks.get() == "Hell Bent for Leather":
            webbrowser.open(('https://music.youtube.com/watch?v=OwUpV1_tteY'), new = 2)
        if self.dainu_boks.get() == "Steeler":
            webbrowser.open(('https://music.youtube.com/watch?v=EnGWEvDXrAE'), new = 2)
        if self.dainu_boks.get() == "Blood Red Skies":
            webbrowser.open(('https://music.youtube.com/watch?v=aORXZiGeIdA'), new = 2)
        if self.dainu_boks.get() == "Metal Meltdown":
            webbrowser.open(('https://music.youtube.com/watch?v=qJS80JB-sn8'), new = 2)
        if self.dainu_boks.get() == "Holy Diver":
            webbrowser.open(('https://music.youtube.com/watch?v=uDtgnYZsw7A'), new = 2)
        if self.dainu_boks.get() == "Rainbow in the Dark":
            webbrowser.open(('https://music.youtube.com/watch?v=7XyHOdMvHg0'), new = 2)
        if self.dainu_boks.get() == "The Last in Line":
            webbrowser.open(('https://music.youtube.com/watch?v=OjvZvRVk8Z0'), new = 2)
        if self.dainu_boks.get() == "Night People":
            webbrowser.open(('https://music.youtube.com/watch?v=Im-O4wXD0pg'), new = 2)
        if self.dainu_boks.get() == "The Eyes":
            webbrowser.open(('https://music.youtube.com/watch?v=jRCS-wT5wE4'), new = 2)
        if self.dainu_boks.get() == "Straight Through the Heart":
            webbrowser.open(('https://music.youtube.com/watch?v=0wfgdSZ4TIk'), new = 2)
        if self.dainu_boks.get() == "Stand Up and Shout":
            webbrowser.open(('https://music.youtube.com/watch?v=XhlkabrJIy8'), new = 2)
        if self.dainu_boks.get() == "Killing the Dragon":
            webbrowser.open(('https://music.youtube.com/watch?v=12UCCXufGjk'), new = 2)
        if self.dainu_boks.get() == "Dream Evil":
            webbrowser.open(('https://music.youtube.com/watch?v=WUqDezHZ7B0'), new = 2)
        if self.dainu_boks.get() == "Shivers":
            webbrowser.open(('https://music.youtube.com/watch?v=FYJJwW1RETI'), new = 2)
        if self.dainu_boks.get() == "The Crusader":
            webbrowser.open(('https://music.youtube.com/watch?v=4AdP6WtYZ9Y'), new = 2)
        if self.dainu_boks.get() == "Broken Heroes":
            webbrowser.open(('https://music.youtube.com/watch?v=p1-tYaTboig'), new = 2)
        if self.dainu_boks.get() == "Wheels of Steel":
            webbrowser.open(('https://music.youtube.com/watch?v=mKlF9o2R3cI'), new = 2)
        if self.dainu_boks.get() == "Power & The Glory":
            webbrowser.open(('https://music.youtube.com/watch?v=xWt88OQJRyQ'), new = 2)
        if self.dainu_boks.get() == "Just Let Me Rock":
            webbrowser.open(('https://music.youtube.com/watch?v=wrJsq_YKQvU'), new = 2)
        if self.dainu_boks.get() == "Denim and Leather":
            webbrowser.open(('https://music.youtube.com/watch?v=hFly5TwDKOg'), new = 2)
        if self.dainu_boks.get() == "Midnight Rider":
            webbrowser.open(('https://music.youtube.com/watch?v=ipdGIk4N6dA'), new = 2)
        if self.dainu_boks.get() == "Metalhead":
            webbrowser.open(('https://music.youtube.com/watch?v=3dvxZju0CPo'), new = 2)
        if self.dainu_boks.get() == "Set Me Free":
            webbrowser.open(('https://music.youtube.com/watch?v=5F-cPa_YBdE'), new = 2)
        if self.dainu_boks.get() == "Midas Touch":
            webbrowser.open(('https://music.youtube.com/watch?v=Byr9Td7P8eQ'), new = 2)

    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Iron Maiden":
            self.dainu_boks.config(value = self.ironm_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Black Sabbath":
            self.dainu_boks.config(value = self.blacksab_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Judas Priest":
            self.dainu_boks.config(value = self.judas_priest_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Dio":
            self.dainu_boks.config(value = self.dio_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Saxon":
            self.dainu_boks.config(value = self.saxon_dainos)
            self.dainu_boks.current(0)

    def open_ironm(self):
        self.random_ironm = ['https://music.youtube.com/watch?v=bePCRKGUwAY',
                            'https://music.youtube.com/watch?v=HAQQUDbuudY',
                            'https://music.youtube.com/watch?v=W4DfbinBgL4',
                            'https://music.youtube.com/watch?v=Q_XJ-7jNqws',
                            'https://music.youtube.com/watch?v=ULsr-fFVjVs',
                            'https://music.youtube.com/watch?v=Mw-o_cSdqmI',
                            'https://music.youtube.com/watch?v=YCmUqAffWS8',
                            'https://music.youtube.com/watch?v=oNwOA84zAcE',
                            'https://music.youtube.com/watch?v=X5P_muGUJR4',
                            'https://music.youtube.com/watch?v=jThfgcOqwlY'
                        ]
        webbrowser.open(choice(self.random_ironm), new = 2)

    def open_black_sab(self):
        self.random_blacksab = ['https://music.youtube.com/watch?v=m7nwbJLO9qo',
                                'https://music.youtube.com/watch?v=9kgQQuPZ8K0',
                                'https://music.youtube.com/watch?v=-R5XnrZn47Q',
                                'https://music.youtube.com/watch?v=cYZE4vKDqzs',
                                'https://music.youtube.com/watch?v=_eBCxYVma1g',
                                'https://music.youtube.com/watch?v=b3-QqGVt-tM',
                                'https://music.youtube.com/watch?v=VcLRrG0W9hE',
                                'https://music.youtube.com/watch?v=f-e8-DUqt0I',
                                'https://music.youtube.com/watch?v=kkcHZQ_hZWk',
                                'https://music.youtube.com/watch?v=0BXG1zvBWKo'
                            ]
        webbrowser.open(choice(self.random_blacksab), new = 2)

    def open_judasp(self):
        self.random_judasp = ['https://music.youtube.com/watch?v=4s1gBIVOTtk',
                            'https://music.youtube.com/watch?v=BXtPycm5dGc',
                            'https://music.youtube.com/watch?v=PjTLOaD6fr4',
                            'https://music.youtube.com/watch?v=XUiTEob4Kzg',
                            'https://music.youtube.com/watch?v=dp-KXWfisHA',
                            'https://music.youtube.com/watch?v=LNyIhirtXUI',
                            'https://music.youtube.com/watch?v=OwUpV1_tteY',
                            'https://music.youtube.com/watch?v=EnGWEvDXrAE',
                            'https://music.youtube.com/watch?v=aORXZiGeIdA',
                            'https://music.youtube.com/watch?v=qJS80JB-sn8'
                        ]
        webbrowser.open(choice(self.random_judasp), new = 2)

    def open_dio(self):
        self.radom_dio = ['https://music.youtube.com/watch?v=uDtgnYZsw7A',
                        'https://music.youtube.com/watch?v=7XyHOdMvHg0',
                        'https://music.youtube.com/watch?v=OjvZvRVk8Z0',
                        'https://music.youtube.com/watch?v=Im-O4wXD0pg',
                        'https://music.youtube.com/watch?v=jRCS-wT5wE4',
                        'https://music.youtube.com/watch?v=0wfgdSZ4TIk',
                        'https://music.youtube.com/watch?v=XhlkabrJIy8',
                        'https://music.youtube.com/watch?v=12UCCXufGjk',
                        'https://music.youtube.com/watch?v=WUqDezHZ7B0',
                        'https://music.youtube.com/watch?v=FYJJwW1RETI'
                    ]
        webbrowser.open(choice(self.radom_dio), new = 2)

    def open_saxon(self):
        self.random_saxon = ['https://music.youtube.com/watch?v=4AdP6WtYZ9Y',
                            'https://music.youtube.com/watch?v=p1-tYaTboig',
                            'https://music.youtube.com/watch?v=mKlF9o2R3cI',
                            'https://music.youtube.com/watch?v=xWt88OQJRyQ',
                            'https://music.youtube.com/watch?v=wrJsq_YKQvU',
                            'https://music.youtube.com/watch?v=hFly5TwDKOg',
                            'https://music.youtube.com/watch?v=ipdGIk4N6dA',
                            'https://music.youtube.com/watch?v=3dvxZju0CPo',
                            'https://music.youtube.com/watch?v=5F-cPa_YBdE',
                            'https://music.youtube.com/watch?v=Byr9Td7P8eQ '
                        ]
        webbrowser.open(choice(self.random_saxon), new = 2)

    def uzdaryti(self):
        self.master.destroy()


class VidinisPunk:
    def __init__(self, master):
        self.master = master
        self.ramones = tk.Button(self.master, text = "Ramones", width = 15, command = self.open_ramones, highlightbackground="MediumPurple4")
        self.sexpistols = tk.Button(self.master, text = "Sex Pistols", width = 15, command = self.open_sex_pistols, highlightbackground="MediumPurple4")
        self.offspring = tk.Button(self.master, text = "The Offspring", width = 15, command = self.open_offspinrg, highlightbackground="MediumPurple4")
        self.misfits = tk.Button(self.master, text = "Misfits", width = 15, command = self.open_misfits, highlightbackground="MediumPurple4")
        self.clash = tk.Button(self.master, text = "The Clash", width = 15, command = self.open_clash, highlightbackground="MediumPurple4")
        self.uzdaryti_punk = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground="MediumPurple4")
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "MediumPurple4")
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "MediumPurple4")
        self.atlikeju_sarasas = ["Ramones", "Sex Pistols", "The Offspring", "Misfits", "The Clash"]
        self.ramondes_dainos = ["Blitzkrieg Bop",
                                "Pet Sematary",
                                "Baby I love You",
                                "I Wanna Be Sedated",
                                "I Don't Wanna Grow Up",
                                "Sheena is a Punk Rocker",
                                "The KKK Took my Baby Away",
                                "Surfin' Bird",
                                "Pinhead",
                                "I am not Jesus"
                            ]
        self.sexpistols_dainos = ["God Save The Queen",
                                "Anarchy in the UK",
                                "Holidays in the Sun",
                                "Bodies",
                                "My Way",
                                "EMI",
                                "Lonely Boy",
                                "No Feelings",
                                "Something Else",
                                "Pretty Vacant"
                            ]
        self.offspring_dainos = ["The Kids Aren't Alright",
                                "Self Esteem",
                                "Why Don't You Get A Job",
                                "Want You Bad",
                                "Pretty Fly",
                                "All I Want",
                                "Come Out and Play",
                                "Americana",
                                "Staring At the Sun",
                                "The Meaning of Life"
                            ]
        self.misfits_dainos = ["Dig Her Bones Up",
                                "Last Caress",
                                "Saturday Night",
                                "Scream",
                                "Die, Die My Darling",
                                "Helena",
                                "Static Age",
                                "Hollywood Babylon",
                                "Shining",
                                "Donna"
                            ]
        self.clash_dainos = ["London Calling",
                            "Should I Stay or Should I Go",
                            "I Fought the Law",
                            "Rock the Casbah",
                            "Spanish Bombs",
                            "Clash City Rockers",
                            "The Magnificent Seven",
                            "Rudie Can't Fail",
                            "This is Radio Clash",
                            "This is England"
                        ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column = 0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column = 1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='MediumPurple4', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan = 2)
        self.uzrasas1.grid(row = 0, columnspan=2)
        self.ramones.grid(row = 1, columnspan=2)
        self.sexpistols.grid(row = 2, columnspan=2)
        self.offspring.grid(row = 3, columnspan=2)
        self.misfits.grid(row = 4, columnspan=2)
        self.clash.grid(row = 5, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        self.uzdaryti_punk.grid(row = 9, columnspan=2)

    def picker(self):
        if self.dainu_boks.get() == "Blitzkrieg Bop":
            webbrowser.open(('https://music.youtube.com/watch?v=skdE0KAFCEA'), new = 2)
        if self.dainu_boks.get() == "Pet Sematary":
            webbrowser.open(('https://music.youtube.com/watch?v=QP4uTN6CXo8'), new = 2)
        if self.dainu_boks.get() == "Baby I love You":
            webbrowser.open(('https://music.youtube.com/watch?v=qO3F5Kayz8I'), new = 2)
        if self.dainu_boks.get() == "I Wanna Be Sedated":
            webbrowser.open(('https://music.youtube.com/watch?v=8O9P5Us_eVo'), new = 2)
        if self.dainu_boks.get() == "I Don't Wanna Grow Up":
            webbrowser.open(('https://music.youtube.com/watch?v=VXTLKfUR72o'), new = 2)
        if self.dainu_boks.get() == "Sheena is a Punk Rocker":
            webbrowser.open(('https://music.youtube.com/watch?v=5CM5YgUBxLw'), new = 2)
        if self.dainu_boks.get() == "The KKK Took my Baby Away":
            webbrowser.open(('https://music.youtube.com/watch?v=pOpdKnoG8hE'), new = 2)
        if self.dainu_boks.get() == "Surfin' Bird":
            webbrowser.open(('https://music.youtube.com/watch?v=Y2ef-HLjElw'), new = 2)
        if self.dainu_boks.get() == "Pinhead":
            webbrowser.open(('https://music.youtube.com/watch?v=whIMah7Yi_4'), new = 2)
        if self.dainu_boks.get() == "I am not Jesus":
            webbrowser.open(('https://music.youtube.com/watch?v=5AvUUPZnYNs'), new = 2)
        if self.dainu_boks.get() == "God Save The Queen":
            webbrowser.open(('https://music.youtube.com/watch?v=nE-AXzHFT1U'), new = 2)
        if self.dainu_boks.get() == "Anarchy in the UK":
            webbrowser.open(('https://music.youtube.com/watch?v=YJRnwaEUNkM'), new = 2)
        if self.dainu_boks.get() == "Holidays in the Sun":
            webbrowser.open(('https://music.youtube.com/watch?v=r7_KZE0y5e8'), new = 2)
        if self.dainu_boks.get() == "Bodies":
            webbrowser.open(('https://music.youtube.com/watch?v=3EqT5E609oU'), new = 2)
        if self.dainu_boks.get() == "My Way":
            webbrowser.open(('https://music.youtube.com/watch?v=qzlt-nO74qk'), new = 2)
        if self.dainu_boks.get() == "EMI":
            webbrowser.open(('https://music.youtube.com/watch?v=Jb1cOIk3sDw'), new = 2)
        if self.dainu_boks.get() == "Lonely Boy":
            webbrowser.open(('https://music.youtube.com/watch?v=QJxxiCJCbUM'), new = 2)
        if self.dainu_boks.get() == "No Feelings":
            webbrowser.open(('https://music.youtube.com/watch?v=GxAD3AyRSyc'), new = 2)
        if self.dainu_boks.get() == "Something Else":
            webbrowser.open(('https://music.youtube.com/watch?v=vjRA5Blr55Q'), new = 2)
        if self.dainu_boks.get() == "Pretty Vacant":
            webbrowser.open(('https://music.youtube.com/watch?v=RBFLY-SR_w4'), new = 2)
        if self.dainu_boks.get() == "The Kids Aren't Alright":
            webbrowser.open(('https://music.youtube.com/watch?v=-uQi0vJK9lk'), new = 2)
        if self.dainu_boks.get() == "Self Esteem":
            webbrowser.open(('https://music.youtube.com/watch?v=7ifeDVAE_Zg'), new = 2)
        if self.dainu_boks.get() == "Why Don't You Get A Job":
            webbrowser.open(('https://music.youtube.com/watch?v=mQYJYY4VkWA'), new = 2)
        if self.dainu_boks.get() == "Want You Bad":
            webbrowser.open(('https://music.youtube.com/watch?v=hnno3h-ZW_8'), new = 2)
        if self.dainu_boks.get() == "Pretty Fly":
            webbrowser.open(('https://music.youtube.com/watch?v=BepGmpLT9HA'), new = 2)
        if self.dainu_boks.get() == "All I Want":
            webbrowser.open(('https://music.youtube.com/watch?v=ldGdFnvSCSQ'), new = 2)
        if self.dainu_boks.get() == "Come Out and Play":
            webbrowser.open(('https://music.youtube.com/watch?v=V92CRYaOQCI'), new = 2)
        if self.dainu_boks.get() == "Americana":
            webbrowser.open(('https://music.youtube.com/watch?v=GtzKW_ONjJ0'), new = 2)
        if self.dainu_boks.get() == "Staring At the Sun":
            webbrowser.open(('https://music.youtube.com/watch?v=R1xM-r4TF6Q'), new = 2)
        if self.dainu_boks.get() == "The Meaning of Life":
            webbrowser.open(('https://music.youtube.com/watch?v=3Os_bMAcZ6w'), new = 2)
        if self.dainu_boks.get() == "Dig Her Bones Up":
            webbrowser.open(('https://music.youtube.com/watch?v=RgwZ76_-0sw'), new = 2)
        if self.dainu_boks.get() == "Last Caress":
            webbrowser.open(('https://music.youtube.com/watch?v=UuzA4U1njO8'), new = 2)
        if self.dainu_boks.get() == "Saturday Night":
            webbrowser.open(('https://music.youtube.com/watch?v=JlWPpQmjnVQ'), new = 2)
        if self.dainu_boks.get() == "Scream":
            webbrowser.open(('https://music.youtube.com/watch?v=GHKWwQMsDpY'), new = 2)
        if self.dainu_boks.get() == "Die, Die My Darling":
            webbrowser.open(('https://music.youtube.com/watch?v=AMYt_GntfnE'), new = 2)
        if self.dainu_boks.get() == "Helena":
            webbrowser.open(('https://music.youtube.com/watch?v=g2qCdXE21og'), new = 2)
        if self.dainu_boks.get() == "Static Age":
            webbrowser.open(('https://music.youtube.com/watch?v=Ckw8jB2VFUM'), new = 2)
        if self.dainu_boks.get() == "Hollywood Babylon":
            webbrowser.open(('https://music.youtube.com/watch?v=GSpZUCUXzQE'), new = 2)
        if self.dainu_boks.get() == "Shining":
            webbrowser.open(('https://music.youtube.com/watch?v=npIouDk6J2g'), new = 2)
        if self.dainu_boks.get() == "Donna":
            webbrowser.open(('https://music.youtube.com/watch?v=ynmK-j2Db6k'), new = 2)
        if self.dainu_boks.get() == "London Calling":
            webbrowser.open(('https://music.youtube.com/watch?v=XN7iEFVLf5c'), new = 2)
        if self.dainu_boks.get() == "Should I Stay or Should I Go":
            webbrowser.open(('https://music.youtube.com/watch?v=wjZMcWaniA4'), new = 2)
        if self.dainu_boks.get() == "I Fought the Law":
            webbrowser.open(('https://music.youtube.com/watch?v=yhcreVY_qLI'), new = 2)
        if self.dainu_boks.get() == "Rock the Casbah":
            webbrowser.open(('https://music.youtube.com/watch?v=0pCFVX6lzHU'), new = 2)
        if self.dainu_boks.get() == "Spanish Bombs":
            webbrowser.open(('https://music.youtube.com/watch?v=KuKtSzqx9i8'), new = 2)
        if self.dainu_boks.get() == "Clash City Rockers":
            webbrowser.open(('https://music.youtube.com/watch?v=lvmoVYGUQKQ'), new = 2)
        if self.dainu_boks.get() == "The Magnificent Seven":
            webbrowser.open(('https://music.youtube.com/watch?v=-Aj92HNB8Tc'), new = 2)
        if self.dainu_boks.get() == "Rudie Can't Fail":
            webbrowser.open(('https://music.youtube.com/watch?v=_MgIEKfG0LE'), new = 2)
        if self.dainu_boks.get() == "This is Radio Clash":
            webbrowser.open(('https://music.youtube.com/watch?v=pc4rzuAhwsI'), new = 2)
        if self.dainu_boks.get() == "This is England":
            webbrowser.open(('https://music.youtube.com/watch?v=qkj0wUcbUeE'), new = 2)
        

    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Ramones":
            self.dainu_boks.config(value = self.ramondes_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Sex Pistols":
            self.dainu_boks.config(value = self.sexpistols_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "The Offspring":
            self.dainu_boks.config(value = self.offspring_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Misfits":
            self.dainu_boks.config(value = self.misfits_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "The Clash":
            self.dainu_boks.config(value = self.clash_dainos)
            self.dainu_boks.current(0)
    
    def open_ramones(self):
        self.random_ramones = ['https://music.youtube.com/watch?v=skdE0KAFCEA',
                                'https://music.youtube.com/watch?v=QP4uTN6CXo8', 
                                'https://music.youtube.com/watch?v=qO3F5Kayz8I',
                                'https://music.youtube.com/watch?v=8O9P5Us_eVo',
                                'https://music.youtube.com/watch?v=VXTLKfUR72o',
                                'https://music.youtube.com/watch?v=5CM5YgUBxLw',
                                'https://music.youtube.com/watch?v=pOpdKnoG8hE',
                                'https://music.youtube.com/watch?v=Y2ef-HLjElw',
                                'https://music.youtube.com/watch?v=whIMah7Yi_4',
                                'https://music.youtube.com/watch?v=5AvUUPZnYNs'
                            ]
        webbrowser.open(choice(self.random_ramones), new = 2)

    
    def open_sex_pistols(self):
        self.random_sex_pistols = ['https://music.youtube.com/watch?v=nE-AXzHFT1U',
                                    'https://music.youtube.com/watch?v=YJRnwaEUNkM',
                                    'https://music.youtube.com/watch?v=r7_KZE0y5e8',
                                    'https://music.youtube.com/watch?v=3EqT5E609oU',
                                    'https://music.youtube.com/watch?v=qzlt-nO74qk',
                                    'https://music.youtube.com/watch?v=Jb1cOIk3sDw',
                                    'https://music.youtube.com/watch?v=QJxxiCJCbUM',
                                    'https://music.youtube.com/watch?v=GxAD3AyRSyc',
                                    'https://music.youtube.com/watch?v=vjRA5Blr55Q',
                                    'https://music.youtube.com/watch?v=RBFLY-SR_w4'
                                ]
        webbrowser.open(choice(self.random_sex_pistols), new = 2)

    def open_offspinrg(self):
        self.random_offspring = ['https://music.youtube.com/watch?v=-uQi0vJK9lk',
                                'https://music.youtube.com/watch?v=7ifeDVAE_Zg',
                                'https://music.youtube.com/watch?v=mQYJYY4VkWA',
                                'https://music.youtube.com/watch?v=hnno3h-ZW_8',
                                'https://music.youtube.com/watch?v=BepGmpLT9HA',
                                'https://music.youtube.com/watch?v=ldGdFnvSCSQ',
                                'https://music.youtube.com/watch?v=V92CRYaOQCI',
                                'https://music.youtube.com/watch?v=GtzKW_ONjJ0',
                                'https://music.youtube.com/watch?v=R1xM-r4TF6Q',
                                'https://music.youtube.com/watch?v=3Os_bMAcZ6w'
                            ]       
        webbrowser.open(choice(self.random_offspring), new = 2)

    def open_misfits(self):
        self.random_misfits = ['https://music.youtube.com/watch?v=RgwZ76_-0sw',
                                'https://music.youtube.com/watch?v=UuzA4U1njO8',
                                'https://music.youtube.com/watch?v=JlWPpQmjnVQ',
                                'https://music.youtube.com/watch?v=GHKWwQMsDpY',
                                'https://music.youtube.com/watch?v=AMYt_GntfnE',
                                'https://music.youtube.com/watch?v=g2qCdXE21og',
                                'https://music.youtube.com/watch?v=Ckw8jB2VFUM',
                                'https://music.youtube.com/watch?v=GSpZUCUXzQE',
                                'https://music.youtube.com/watch?v=npIouDk6J2g',
                                'https://music.youtube.com/watch?v=ynmK-j2Db6k'
                            ]
        webbrowser.open(choice(self.random_misfits), new = 2)

    
    def open_clash(self):
        self.random_clash = ['https://music.youtube.com/watch?v=XN7iEFVLf5c',
                            'https://music.youtube.com/watch?v=wjZMcWaniA4',
                            'https://music.youtube.com/watch?v=yhcreVY_qLI',
                            'https://music.youtube.com/watch?v=0pCFVX6lzHU',
                            'https://music.youtube.com/watch?v=KuKtSzqx9i8',
                            'https://music.youtube.com/watch?v=lvmoVYGUQKQ',
                            'https://music.youtube.com/watch?v=-Aj92HNB8Tc',
                            'https://music.youtube.com/watch?v=_MgIEKfG0LE',
                            'https://music.youtube.com/watch?v=pc4rzuAhwsI',
                            'https://music.youtube.com/watch?v=qkj0wUcbUeE'
                        ]
        webbrowser.open(choice(self.random_clash), new = 2)

    def uzdaryti(self):
        self.master.destroy()

class VidinisBlackMetal:
    def __init__(self, master):
        self.master = master
        self.mayhem = tk.Button(self.master, text = "Mayhem", width = 15, command = self.open_mayhem, highlightbackground='midnight blue')
        self.marduk = tk.Button(self.master, text = "Marduk", width = 15, command = self.open_marduk, highlightbackground='midnight blue')
        self.luctus = tk.Button(self.master, text = "Luctus", width = 15, command = self.open_luctus, highlightbackground='midnight blue')
        self.watain = tk.Button(self.master, text = "Watain", width = 15, command = self.open_watain, highlightbackground='midnight blue')
        self.behemoth = tk.Button(self.master, text = "Behemoth", width = 15, command = self.open_behemoth, highlightbackground='midnight blue')
        self.uzdaryti_bmetal = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='midnight blue')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "midnight blue")
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "midnight blue")
        self.atlikeju_sarasas = ["Mayhem", "Marduk", "Luctus", "Watain", "Behemoth"]
        self.mayhem_dainos = ["Freezing Moon",
                            "Deathcrush",
                            "Pagan Fears",
                            "Funeral Fog",
                            "De Mysteriis Dom Sathanas",
                            "Necrolust",
                            "A Grand Declaration of War",
                            "Ancient Skin",
                            "Life Etarnal",
                            "Dark Night of the Soul"
                        ]
        self.marduk_dainos = ["Souls for Belial",
                            "Panzer Division Marduk",
                            "Frontschwein",
                            "World of Blades",
                            "Samhain",
                            "Seven Angels, Seven Trumpets",
                            "Azreal",
                            "World Funeral",
                            "Africa",
                            "Steel Inferno"
                        ]
        self.luctus_dainos = ["Nežiūrėk nežibėk",
                            "Tikrovės Iliuzija",
                            "Akimirka Prieš Mirtį",
                            "Bedvasiai",
                            "Kvantinis Šuolis",
                            "Stotis",
                            "Mirusių Žvaigždžių Šviesoj",
                            "Eilinio Mirtis",
                            "Už Lietuvą!",
                            "Kas Tu Esi?"
                        ]
        self.watain_dainos = ["Malfeitor",
                            "They Rode On",
                            "Legions of the Black Light",
                            "The Wild Hunt",
                            "Serimosa",
                            "Nuclear Alchemy",
                            "Devil's Blood",
                            "Satan's Hunger",
                            "Wolves Curse",
                            "Beyond"
                        ]
        self.behemoth_dainos = ["Ov Fire and the Void",
                                "O Father O Stan O Sun",
                                "Blow Your Trumpets Gabriel",
                                "Deathless Sun",
                                "At the Left Hand Ov God",
                                "The Satanist",
                                "Demigod",
                                "Ben Sahar",
                                "Solve",
                                "Decade of Therion"
                            ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column = 0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column = 1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='midnight blue', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan=2)
        self.uzrasas1.grid(row = 0, columnspan=2)
        self.mayhem.grid(row = 1, columnspan=2)
        self.marduk.grid(row = 2, columnspan=2)
        self.luctus.grid(row = 3, columnspan=2)
        self.watain.grid(row = 4, columnspan=2)
        self.behemoth.grid(row = 5, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        self.uzdaryti_bmetal.grid(row = 9, columnspan=2)


    def picker(self):
        if self.dainu_boks.get() == "Freezing Moon":
            webbrowser.open(('https://music.youtube.com/watch?v=9emO9qo4FwE'), new = 2)
        if self.dainu_boks.get() == "Deathcrush":
            webbrowser.open(('https://music.youtube.com/watch?v=Dgzmgk9IhAA'), new = 2)
        if self.dainu_boks.get() == "Pagan Fears":
            webbrowser.open(('https://music.youtube.com/watch?v=f7cQNoMFv0g'), new = 2)
        if self.dainu_boks.get() == "Funeral Fog":
            webbrowser.open(('https://music.youtube.com/watch?v=q5TiZO6Na_M'), new = 2)
        if self.dainu_boks.get() == "De Mysteriis Dom Sathanas":
            webbrowser.open(('https://music.youtube.com/watch?v=zNs4zSKK9S4'), new = 2)
        if self.dainu_boks.get() == "Necrolust":
            webbrowser.open(('https://music.youtube.com/watch?v=z0agoBcAF1c'), new = 2)
        if self.dainu_boks.get() == "A Grand Declaration of War":
            webbrowser.open(('https://music.youtube.com/watch?v=fUPRdtw3myw'), new = 2)
        if self.dainu_boks.get() == "Ancient Skin":
            webbrowser.open(('https://music.youtube.com/watch?v=tSfBXpfwRJs'), new = 2)
        if self.dainu_boks.get() == "Life Etarnal":
            webbrowser.open(('https://music.youtube.com/watch?v=DJtPCuQyTSk'), new = 2)
        if self.dainu_boks.get() == "Dark Night of the Soul":
            webbrowser.open(('https://music.youtube.com/watch?v=_vEAZQZEIBk'), new = 2)
        if self.dainu_boks.get() == "Souls for Belial":
            webbrowser.open(('https://music.youtube.com/watch?v=uWk7QDaNKQw'), new = 2)
        if self.dainu_boks.get() == "Panzer Division Marduk":
            webbrowser.open(('https://music.youtube.com/watch?v=sDNdtU_wc74'), new = 2)
        if self.dainu_boks.get() == "Frontschwein":
            webbrowser.open(('https://music.youtube.com/watch?v=0jZ7JsLuw6I'), new = 2)
        if self.dainu_boks.get() == "World of Blades":
            webbrowser.open(('https://music.youtube.com/watch?v=eUh4YwJhydk'), new = 2)
        if self.dainu_boks.get() == "Samhain":
            webbrowser.open(('https://music.youtube.com/watch?v=9j5UmXXZqwk'), new = 2)
        if self.dainu_boks.get() == "Seven Angels, Seven Trumpets":
            webbrowser.open(('https://music.youtube.com/watch?v=2AR-GcoJUdk'), new = 2)
        if self.dainu_boks.get() == "Azreal":
            webbrowser.open(('https://music.youtube.com/watch?v=0AyqNRDyxR4'), new = 2)
        if self.dainu_boks.get() == "World Funeral":
            webbrowser.open(('https://music.youtube.com/watch?v=FCoQyLWahI8'), new = 2)
        if self.dainu_boks.get() == "Africa":
            webbrowser.open(('https://music.youtube.com/watch?v=yvdhNrzWGtA'), new = 2)
        if self.dainu_boks.get() == "Steel Inferno":
            webbrowser.open(('https://music.youtube.com/watch?v=llp-X-axKQs'), new = 2)
        if self.dainu_boks.get() == "Nežiūrėk nežibėk":
            webbrowser.open(('https://music.youtube.com/watch?v=0-kJpZZQeSY'), new = 2)
        if self.dainu_boks.get() == "Tikrovės Iliuzija":
            webbrowser.open(('https://music.youtube.com/watch?v=s-qRfeOVrSk'), new = 2)
        if self.dainu_boks.get() == "Akimirka Prieš Mirtį":
            webbrowser.open(('https://music.youtube.com/watch?v=-ZdnW7fw_f4'), new = 2)
        if self.dainu_boks.get() == "Bedvasiai":
            webbrowser.open(('https://music.youtube.com/watch?v=HbVy07QInQU'), new = 2)
        if self.dainu_boks.get() == "Kvantinis Šuolis":
            webbrowser.open(('https://music.youtube.com/watch?v=4mGfO6Q6DBE'), new = 2)
        if self.dainu_boks.get() == "Stotis":
            webbrowser.open(('https://music.youtube.com/watch?v=dRhx9VgpFWE'), new = 2)
        if self.dainu_boks.get() == "Mirusių Žvaigždžių Šviesoj":
            webbrowser.open(('https://music.youtube.com/watch?v=T3oXuAxf2fw'), new = 2)
        if self.dainu_boks.get() == "Eilinio Mirtis":
            webbrowser.open(('https://music.youtube.com/watch?v=Hc1OZQmc_bc'), new = 2)
        if self.dainu_boks.get() == "Už Lietuvą!":
            webbrowser.open(('https://music.youtube.com/watch?v=Gjtx7kTILW8'), new = 2)
        if self.dainu_boks.get() == "Kas Tu Esi?":
            webbrowser.open(('https://music.youtube.com/watch?v=ADdJ4UHGdjo'), new = 2)
        if self.dainu_boks.get() == "Malfeitor":
            webbrowser.open(('https://music.youtube.com/watch?v=QZJolwCj1Tc'), new = 2)
        if self.dainu_boks.get() == "They Rode On":
            webbrowser.open(('https://music.youtube.com/watch?v=y1shqeyKVPI'), new = 2)
        if self.dainu_boks.get() == "Legions of the Black Light":
            webbrowser.open(('https://music.youtube.com/watch?v=gMjzuY_OpvE'), new = 2)
        if self.dainu_boks.get() == "The Wild Hunt":
            webbrowser.open(('https://music.youtube.com/watch?v=utukmmZpGHM'), new = 2)
        if self.dainu_boks.get() == "Serimosa":
            webbrowser.open(('https://music.youtube.com/watch?v=NQlG091nQLA'), new = 2)
        if self.dainu_boks.get() == "Nuclear Alchemy":
            webbrowser.open(('https://music.youtube.com/watch?v=9dRdUsZ7JBA'), new = 2)
        if self.dainu_boks.get() == "Devil's Blood":
            webbrowser.open(('https://music.youtube.com/watch?v=LBsPaP3VwW0'), new = 2)
        if self.dainu_boks.get() == "Satan's Hunger":
            webbrowser.open(('https://music.youtube.com/watch?v=Z_itZMagBsg'), new = 2)
        if self.dainu_boks.get() == "Wolves Curse":
            webbrowser.open(('https://music.youtube.com/watch?v=MHk1jKZoYz4'), new = 2)
        if self.dainu_boks.get() == "Beyond":
            webbrowser.open(('https://music.youtube.com/watch?v=dbAVc1v2sMU'), new = 2)
        if self.dainu_boks.get() == "Ov Fire and the Void":
            webbrowser.open(('https://music.youtube.com/watch?v=uoCIX4H0FIE'), new = 2)
        if self.dainu_boks.get() == "O Father O Stan O Sun":
            webbrowser.open(('https://music.youtube.com/watch?v=NfFSl2DUojc'), new = 2)
        if self.dainu_boks.get() == "Blow Your Trumpets Gabriel":
            webbrowser.open(('https://music.youtube.com/watch?v=Txgv6IaD4kk'), new = 2)
        if self.dainu_boks.get() == "Deathless Sun":
            webbrowser.open(('https://music.youtube.com/watch?v=l4I3HditvPk'), new = 2)
        if self.dainu_boks.get() == "At the Left Hand Ov God":
            webbrowser.open(('https://music.youtube.com/watch?v=N70k7PikaWk'), new = 2)
        if self.dainu_boks.get() == "The Satanist":
            webbrowser.open(('https://music.youtube.com/watch?v=7CQTBItq110'), new = 2)
        if self.dainu_boks.get() == "Demigod":
            webbrowser.open(('https://music.youtube.com/watch?v=_znQvXC3uw4'), new = 2)
        if self.dainu_boks.get() == "Ben Sahar":
            webbrowser.open(('https://music.youtube.com/watch?v=6pulvL2rbmk'), new = 2)
        if self.dainu_boks.get() == "Solve":
            webbrowser.open(('https://music.youtube.com/watch?v=NERGLk8tyPs'), new = 2)
        if self.dainu_boks.get() == "Decade of Therion":
            webbrowser.open(('https://music.youtube.com/watch?v=8BAD4t_O61k'), new = 2)
        

    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Mayhem":
            self.dainu_boks.config(value = self.mayhem_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Marduk":
            self.dainu_boks.config(value = self.marduk_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Luctus":
            self.dainu_boks.config(value = self.luctus_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Watain":
            self.dainu_boks.config(value = self.watain_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Behemoth":
            self.dainu_boks.config(value = self.behemoth_dainos)
            self.dainu_boks.current(0)


    def open_mayhem(self):
        self.random_mayhem = ['https://music.youtube.com/watch?v=9emO9qo4FwE',
                            'https://music.youtube.com/watch?v=Dgzmgk9IhAA',
                            'https://music.youtube.com/watch?v=f7cQNoMFv0g',
                            'https://music.youtube.com/watch?v=q5TiZO6Na_M',
                            'https://music.youtube.com/watch?v=zNs4zSKK9S4',
                            'https://music.youtube.com/watch?v=z0agoBcAF1c',
                            'https://music.youtube.com/watch?v=fUPRdtw3myw',
                            'https://music.youtube.com/watch?v=tSfBXpfwRJs',
                            'https://music.youtube.com/watch?v=DJtPCuQyTSk',
                            'https://music.youtube.com/watch?v=_vEAZQZEIBk'
                        ]
        webbrowser.open(choice(self.random_mayhem), new = 2)

    def open_marduk(self):
        self.random_marduk = ['https://music.youtube.com/watch?v=uWk7QDaNKQw',
                            'https://music.youtube.com/watch?v=sDNdtU_wc74',
                            'https://music.youtube.com/watch?v=0jZ7JsLuw6I',
                            'https://music.youtube.com/watch?v=eUh4YwJhydk',
                            'https://music.youtube.com/watch?v=9j5UmXXZqwk',
                            'https://music.youtube.com/watch?v=2AR-GcoJUdk',
                            'https://music.youtube.com/watch?v=0AyqNRDyxR4',
                            'https://music.youtube.com/watch?v=FCoQyLWahI8',
                            'https://music.youtube.com/watch?v=yvdhNrzWGtA',
                            'https://music.youtube.com/watch?v=llp-X-axKQs'
                        ]
        webbrowser.open(choice(self.random_marduk), new = 2)

    def open_luctus(self):
        self.random_luctus = ['https://music.youtube.com/watch?v=0-kJpZZQeSY',
                            'https://music.youtube.com/watch?v=s-qRfeOVrSk',
                            'https://music.youtube.com/watch?v=-ZdnW7fw_f4',
                            'https://music.youtube.com/watch?v=HbVy07QInQU',
                            'https://music.youtube.com/watch?v=4mGfO6Q6DBE',
                            'https://music.youtube.com/watch?v=dRhx9VgpFWE',
                            'https://music.youtube.com/watch?v=T3oXuAxf2fw',
                            'https://music.youtube.com/watch?v=Hc1OZQmc_bc',
                            'https://music.youtube.com/watch?v=Gjtx7kTILW8',
                            'https://music.youtube.com/watch?v=ADdJ4UHGdjo'
                        ]
        webbrowser.open(choice(self.random_luctus), new = 2)

    def open_watain(self):
        self.random_watain = ['https://music.youtube.com/watch?v=QZJolwCj1Tc',
                            'https://music.youtube.com/watch?v=y1shqeyKVPI',
                            'https://music.youtube.com/watch?v=gMjzuY_OpvE',
                            'https://music.youtube.com/watch?v=utukmmZpGHM',
                            'https://music.youtube.com/watch?v=NQlG091nQLA',
                            'https://music.youtube.com/watch?v=9dRdUsZ7JBA',
                            'https://music.youtube.com/watch?v=LBsPaP3VwW0',
                            'https://music.youtube.com/watch?v=Z_itZMagBsg',
                            'https://music.youtube.com/watch?v=MHk1jKZoYz4',
                            'https://music.youtube.com/watch?v=dbAVc1v2sMU'
                        ]
        webbrowser.open(choice(self.random_watain), new = 2)

    def open_behemoth(self):
        self.random_behemoth = ['https://music.youtube.com/watch?v=uoCIX4H0FIE',
                                'https://music.youtube.com/watch?v=NfFSl2DUojc',
                                'https://music.youtube.com/watch?v=Txgv6IaD4kk',
                                'https://music.youtube.com/watch?v=l4I3HditvPk',
                                'https://music.youtube.com/watch?v=N70k7PikaWk',
                                'https://music.youtube.com/watch?v=7CQTBItq110',
                                'https://music.youtube.com/watch?v=_znQvXC3uw4',
                                'https://music.youtube.com/watch?v=6pulvL2rbmk',
                                'https://music.youtube.com/watch?v=NERGLk8tyPs',
                                'https://music.youtube.com/watch?v=8BAD4t_O61k'
                            ]
        webbrowser.open(choice(self.random_behemoth), new = 2)

    def uzdaryti(self):
        self.master.destroy()


class VidinisRap:
    def __init__(self, master):
        self.master = master
        self.eminem = tk.Button(self.master, text = "Eminem", width = 15, command = self.open_eminem, highlightbackground='IndianRed4')
        self.snoop = tk.Button(self.master, text = "Snoop Dog", width = 15, command = self.open_snoop_dog, highlightbackground='IndianRed4')
        self.pac = tk.Button(self.master, text = "2Pac", width = 15, command = self.open_2pac, highlightbackground='IndianRed4')
        self.nwa = tk.Button(self.master, text = "N.W.A.", width = 15, command = self.open_nwa, highlightbackground='IndianRed4')
        self.lamar = tk.Button(self.master, text = "Kendrick Lamar", width = 15, command = self.open_kendric, highlightbackground='IndianRed4')
        self.uzdaryti_rap = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='IndianRed4')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = 'IndianRed4')
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = 'IndianRed4')
        self.atlikeju_sarasas = ["Eminem", "Snoop Dog", "2Pac", "N.W.A.", "Kendrick Lamar"]
        self.eminem_dainos = ["Stan",
                            "Without Me",
                            "Lose Yourself",
                            "Not Afraid",
                            "Mockingbird",
                            "When I am Gone",
                            "The Real Slim Shady",
                            "Rap God",
                            "Till' I Collapse",
                            "Drips"
                        ]
        self.snoop_dog_dainos = ["Drop it Like it's Hot",
                                "Sensual Seduction",
                                "Nuthin' but A-G Thing",
                                "Who Am I?",
                                "Gin & Juice",
                                "Vato",
                                "A Bitch I Knew",
                                "Crazy",
                                "Boom",
                                "Smoke the Weed"
                            ]
        self.pac_dainos = ["California Love",
                            "Hit'Em Up",
                            "All Eyes On Me",
                            "Hail Mary",
                            "Ambitionz Az a Ridah",
                            "Dear Mama",
                            "Better Dayz",
                            "Do For Love",
                            "Hellrazor",
                            "Ghetto Gospel"
                        ]
        self.nwa_dainos = ["Fuck Tha Police",
                            "Straight Outta Compton",
                            "Gangsta Gangsta",
                            "Dope Man",
                            "A Bitch Iz A Bitch",
                            "Something 2 Dance 2",
                            "Appetite for Destruction",
                            "Real Niggaz",
                            "8 Ball",
                            "Express Yourself"
                        ]
        self.lamar_dainos = ["m.A.A.d City", 
                            "Humble",
                            "Bitch, Don't KIll My Vibe",
                            "Money Trees",
                            "Swimming Pools",
                            "Pride",
                            "The Heart Part 5",
                            "King Kunta",
                            "DNA",
                            "Poetic Justice"
                        ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column = 0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column = 1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='IndianRed4', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan=2)
        self.uzrasas1.grid(row = 0, columnspan=2)
        self.eminem.grid(row = 1, columnspan=2)
        self.snoop.grid(row = 2, columnspan=2)
        self.pac.grid(row = 3, columnspan=2)
        self.nwa.grid(row = 4, columnspan=2)
        self.lamar.grid(row = 5, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        self.uzdaryti_rap.grid(row = 9, columnspan=2)

    def picker(self):
        if self.dainu_boks.get() == "Stan":
            webbrowser.open(('https://music.youtube.com/watch?v=HIqQ0PfuPo8'), new = 2)
        if self.dainu_boks.get() == "Without Me":
            webbrowser.open(('https://music.youtube.com/watch?v=tqxRidAWER8'), new = 2)
        if self.dainu_boks.get() == "Lose Yourself":
            webbrowser.open(('https://music.youtube.com/watch?v=zlJ0Aj9y67c'), new = 2)
        if self.dainu_boks.get() == "Not Afraid":
            webbrowser.open(('https://music.youtube.com/watch?v=-grPV-Fae6I'), new = 2)
        if self.dainu_boks.get() == "Mockingbird":
            webbrowser.open(('https://music.youtube.com/watch?v=9kznlAwE-8o'), new = 2)
        if self.dainu_boks.get() == "When I am Gone":
            webbrowser.open(('https://music.youtube.com/watch?v=hWqLuSnyqbI'), new = 2)
        if self.dainu_boks.get() == "The Real Slim Shady":
            webbrowser.open(('https://music.youtube.com/watch?v=BdfpV-cIkuA'), new = 2)
        if self.dainu_boks.get() == "Rap God":
            webbrowser.open(('https://music.youtube.com/watch?v=MBJFPq2Llps'), new = 2)
        if self.dainu_boks.get() == "Till' I Collapse":
            webbrowser.open(('https://music.youtube.com/watch?v=Obim8BYGnOE'), new = 2)
        if self.dainu_boks.get() == "Drips":
            webbrowser.open(('https://music.youtube.com/watch?v=HX0qXWwVKEA'), new = 2)
        if self.dainu_boks.get() == "Drop it Like it's Hot":
            webbrowser.open(('https://music.youtube.com/watch?v=ldjajgAHAu4'), new = 2)
        if self.dainu_boks.get() == "Sensual Seduction":
            webbrowser.open(('https://music.youtube.com/watch?v=a1Vunyag-w0'), new = 2)
        if self.dainu_boks.get() == "Nuthin' but A-G Thing":
            webbrowser.open(('https://music.youtube.com/watch?v=ogEUHBUV-bo'), new = 2)
        if self.dainu_boks.get() == "Who Am I?":
            webbrowser.open(('https://music.youtube.com/watch?v=sXx3gtLouNU'), new = 2)
        if self.dainu_boks.get() == "Gin & Juice":
            webbrowser.open(('https://music.youtube.com/watch?v=7qiZ21aL81c'), new = 2)
        if self.dainu_boks.get() == "Vato":
            webbrowser.open(('https://music.youtube.com/watch?v=Inw7B2F6_Hc'), new = 2)
        if self.dainu_boks.get() == "A Bitch I Knew":
            webbrowser.open(('https://music.youtube.com/watch?v=Y3lVNNBTzL8'), new = 2)
        if self.dainu_boks.get() == "Crazy":
            webbrowser.open(('https://music.youtube.com/watch?v=GflVCALGSLQ'), new = 2)
        if self.dainu_boks.get() == "Boom":
            webbrowser.open(('https://music.youtube.com/watch?v=RT8LrkaaSHk'), new = 2)
        if self.dainu_boks.get() == "Smoke the Weed":
            webbrowser.open(('https://music.youtube.com/watch?v=Wo9xc7G9KOg'), new = 2)
        if self.dainu_boks.get() == "California Love":
            webbrowser.open(('https://music.youtube.com/watch?v=LRt6TdSvHag'), new = 2)
        if self.dainu_boks.get() == "Hit'Em Up":
            webbrowser.open(('https://music.youtube.com/watch?v=ugD3_yt756w'), new = 2)
        if self.dainu_boks.get() == "All Eyes On Me":
            webbrowser.open(('https://music.youtube.com/watch?v=zgZ52M4a_R0'), new = 2)
        if self.dainu_boks.get() == "Hail Mary":
            webbrowser.open(('https://music.youtube.com/watch?v=x9bPGZIBt7Y'), new = 2)
        if self.dainu_boks.get() == "Ambitionz Az a Ridah":
            webbrowser.open(('https://music.youtube.com/watch?v=6glk4oMbgKE'), new = 2)
        if self.dainu_boks.get() == "Dear Mama":
            webbrowser.open(('https://music.youtube.com/watch?v=S0Zc8ofInSQ'), new = 2)
        if self.dainu_boks.get() == "Better Dayz":
            webbrowser.open(('https://music.youtube.com/watch?v=Mk2RXIEMK8Y'), new = 2)
        if self.dainu_boks.get() == "Do For Love":
            webbrowser.open(('https://music.youtube.com/watch?v=Y2cWHiKaFjc'), new = 2)
        if self.dainu_boks.get() == "Hellrazor":
            webbrowser.open(('https://music.youtube.com/watch?v=T92u3_z7dS8'), new = 2)
        if self.dainu_boks.get() == "Ghetto Gospel":
            webbrowser.open(('https://music.youtube.com/watch?v=EyBwEbdI0H0'), new = 2)
        if self.dainu_boks.get() == "Fuck Tha Police":
            webbrowser.open(('https://music.youtube.com/watch?v=ADdpLv3RDhA'), new = 2)
        if self.dainu_boks.get() == "Straight Outta Compton":
            webbrowser.open(('https://music.youtube.com/watch?v=9OJStAZz1bc'), new = 2)
        if self.dainu_boks.get() == "Gangsta Gangsta":
            webbrowser.open(('https://music.youtube.com/watch?v=aCAkHFavEdw'), new = 2)
        if self.dainu_boks.get() == "Dope Man":
            webbrowser.open(('https://music.youtube.com/watch?v=yG9aTpyyCaY'), new = 2)
        if self.dainu_boks.get() == "A Bitch Iz A Bitch":
            webbrowser.open(('https://music.youtube.com/watch?v=JRx7R7bcPZs'), new = 2)
        if self.dainu_boks.get() == "Something 2 Dance 2":
            webbrowser.open(('https://music.youtube.com/watch?v=xDRKKMVjgaU'), new = 2)
        if self.dainu_boks.get() == "Appetite for Destruction":
            webbrowser.open(('https://music.youtube.com/watch?v=R1dXVy3Mf7Y'), new = 2)
        if self.dainu_boks.get() == "Real Niggaz":
            webbrowser.open(('https://music.youtube.com/watch?v=6-ihjmlTTeA'), new = 2)
        if self.dainu_boks.get() == "8 Ball":
            webbrowser.open(('https://music.youtube.com/watch?v=TvGYSPv496U'), new = 2)
        if self.dainu_boks.get() == "Express Yourself":
            webbrowser.open(('https://music.youtube.com/watch?v=gHzSpx_9Eww'), new = 2)
        if self.dainu_boks.get() == "m.A.A.d City":
            webbrowser.open(('https://music.youtube.com/watch?v=KKCSwOVudMo'), new = 2)
        if self.dainu_boks.get() == "Humble":
            webbrowser.open(('https://music.youtube.com/watch?v=H4RELGc9su8'), new = 2)
        if self.dainu_boks.get() == "Bitch, Don't KIll My Vibe":
            webbrowser.open(('https://music.youtube.com/watch?v=hDgPW4kIdUI'), new = 2)
        if self.dainu_boks.get() == "Money Trees":
            webbrowser.open(('https://music.youtube.com/watch?v=Iy-dJwHVX84'), new = 2)
        if self.dainu_boks.get() == "Swimming Pools":
            webbrowser.open(('https://music.youtube.com/watch?v=U96f24ueBAo'), new = 2)
        if self.dainu_boks.get() == "Pride":
            webbrowser.open(('https://music.youtube.com/watch?v=pRGmFiEyr0A'), new = 2)
        if self.dainu_boks.get() == "The Heart Part 5":
            webbrowser.open(('https://music.youtube.com/watch?v=kAbhILeXwGE'), new = 2)
        if self.dainu_boks.get() == "King Kunta":
            webbrowser.open(('https://music.youtube.com/watch?v=g0NVaX8DRN4'), new = 2)
        if self.dainu_boks.get() == "DNA":
            webbrowser.open(('https://music.youtube.com/watch?v=Fb3j_yuFh1s'), new = 2)
        if self.dainu_boks.get() == "Poetic Justice":
            webbrowser.open(('https://music.youtube.com/watch?v=TbqmJ5K6iNI'), new = 2)



    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Eminem":
            self.dainu_boks.config(value = self.eminem_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Snoop Dog":
            self.dainu_boks.config(value = self.snoop_dog_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "2Pac":
            self.dainu_boks.config(value = self.pac_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "N.W.A.":
            self.dainu_boks.config(value = self.nwa_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Kendrick Lamar":
            self.dainu_boks.config(value = self.lamar_dainos)
            self.dainu_boks.current(0)

    def open_eminem(self):
        self.random_eminem = ['https://music.youtube.com/watch?v=HIqQ0PfuPo8',
                            'https://music.youtube.com/watch?v=tqxRidAWER8',
                            'https://music.youtube.com/watch?v=zlJ0Aj9y67c',
                            'https://music.youtube.com/watch?v=-grPV-Fae6I',
                            'https://music.youtube.com/watch?v=9kznlAwE-8o',
                            'https://music.youtube.com/watch?v=hWqLuSnyqbI',
                            'https://music.youtube.com/watch?v=BdfpV-cIkuA',
                            'https://music.youtube.com/watch?v=MBJFPq2Llps',
                            'https://music.youtube.com/watch?v=Obim8BYGnOE',
                            'https://music.youtube.com/watch?v=HX0qXWwVKEA'
                        ]
        webbrowser.open(choice(self.random_eminem), new = 2)

    def open_snoop_dog(self):
        self.random_snoop_dog = ['https://music.youtube.com/watch?v=ldjajgAHAu4',
                                'https://music.youtube.com/watch?v=a1Vunyag-w0',
                                'https://music.youtube.com/watch?v=ogEUHBUV-bo',
                                'https://music.youtube.com/watch?v=sXx3gtLouNU',
                                'https://music.youtube.com/watch?v=7qiZ21aL81c',
                                'https://music.youtube.com/watch?v=Inw7B2F6_Hc',
                                'https://music.youtube.com/watch?v=Y3lVNNBTzL8',
                                'https://music.youtube.com/watch?v=GflVCALGSLQ',
                                'https://music.youtube.com/watch?v=RT8LrkaaSHk',
                                'https://music.youtube.com/watch?v=Wo9xc7G9KOg'
                            ]
        webbrowser.open(choice(self.random_snoop_dog), new = 2)

    def open_2pac(self):
        self.random_2pac = ['https://music.youtube.com/watch?v=LRt6TdSvHag',
                            'https://music.youtube.com/watch?v=ugD3_yt756w',
                            'https://music.youtube.com/watch?v=zgZ52M4a_R0',
                            'https://music.youtube.com/watch?v=x9bPGZIBt7Y',
                            'https://music.youtube.com/watch?v=6glk4oMbgKE',
                            'https://music.youtube.com/watch?v=S0Zc8ofInSQ',
                            'https://music.youtube.com/watch?v=Mk2RXIEMK8Y',
                            'https://music.youtube.com/watch?v=Y2cWHiKaFjc',
                            'https://music.youtube.com/watch?v=T92u3_z7dS8',
                            'https://music.youtube.com/watch?v=EyBwEbdI0H0'
                        ]
        webbrowser.open(choice(self.random_2pac), new = 2)

    def open_nwa(self):
        self.random_nwa = ['https://music.youtube.com/watch?v=ADdpLv3RDhA',
                        'https://music.youtube.com/watch?v=9OJStAZz1bc',
                        'https://music.youtube.com/watch?v=aCAkHFavEdw',
                        'https://music.youtube.com/watch?v=yG9aTpyyCaY',
                        'https://music.youtube.com/watch?v=JRx7R7bcPZs',
                        'https://music.youtube.com/watch?v=xDRKKMVjgaU',
                        'https://music.youtube.com/watch?v=R1dXVy3Mf7Y',
                        'https://music.youtube.com/watch?v=6-ihjmlTTeA',
                        'https://music.youtube.com/watch?v=TvGYSPv496U',
                        'https://music.youtube.com/watch?v=gHzSpx_9Eww'
                    ]
        webbrowser.open(choice(self.random_nwa), new = 2)

    def open_kendric(self):
        self.random_kendrick = ['https://music.youtube.com/watch?v=KKCSwOVudMo',
                                'https://music.youtube.com/watch?v=H4RELGc9su8',
                                'https://music.youtube.com/watch?v=hDgPW4kIdUI',
                                'https://music.youtube.com/watch?v=Iy-dJwHVX84',
                                'https://music.youtube.com/watch?v=U96f24ueBAo',
                                'https://music.youtube.com/watch?v=pRGmFiEyr0A',
                                'https://music.youtube.com/watch?v=kAbhILeXwGE',
                                'https://music.youtube.com/watch?v=g0NVaX8DRN4',
                                'https://music.youtube.com/watch?v=Fb3j_yuFh1s',
                                'https://music.youtube.com/watch?v=TbqmJ5K6iNI'
                            ]
        webbrowser.open(choice(self.random_kendrick), new = 2)

    def uzdaryti(self):
        self.master.destroy()


class VidinisPop:
    def __init__(self, master):
        self.master = master
        self.ladygaga = tk.Button(self.master, text = "Lady Gaga", width = 15, command = self.open_ladygaga, highlightbackground='hot pink')
        self.beyonce = tk.Button(self.master, text = "Beyoncé", width = 15, command = self.open_beyonce, highlightbackground='hot pink')
        self.britneysp = tk.Button(self.master, text = "Britney Spears", width = 15, command = self.open_britney, highlightbackground='hot pink')
        self.chaguilera = tk.Button(self.master, text = "Christina Aguilera", width = 15, command = self.open_christina, highlightbackground='hot pink')
        self.justint = tk.Button(self.master, text = "Justin Timberlake", width = 15, command = self.open_justint, highlightbackground='hot pink')
        self.uzdaryti_pop = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='hot pink')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = 'hot pink')
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = 'hot pink')
        self.atlikeju_sarasas = ["Lady Gaga", "Beyoncé", "Britney Spears", "Christina Aguilera", "Justin Timberlake"]
        self.lady_gaga_dainos = ["Bad Romance",
                                "Alejandro",
                                "Hold My Hand",
                                "Poker Face",
                                "Born This Way",
                                "Judas",
                                "Paparazzi",
                                "John Wayne",
                                "Alice",
                                "Love Game"
                            ]
        self.beyonce_dainos = ["Break My Soul", 
                                "Love on Top",
                                "Crazy Love",
                                "Halo",
                                "Single Ladies",
                                "I was Here",
                                "Run the World",
                                "All up in Your Mind",
                                "My Myself and I",
                                "Sorry"
                            ]
        self.britney_dainos = ["Toxic",
                                "Baby One More Time",
                                "Criminal",
                                "Work Bitch",
                                "Opps I did it Again",
                                "Bombastic Love",
                                "Gimme More",
                                "Early Mornin'",
                                "Sometimes",
                                "Piece of Me"
                            ]
        self.aguilera_dainos = ["Dirrty",
                                "Genie in a Bottle",
                                "Hurt",
                                "I turn to You",
                                "Fighter",
                                "Candyman",
                                "Your Body",
                                "Haunted Heart",
                                "Ven Conmingo",
                                "Welcome"
                            ]
        self.timberlake_dainos = ["Mirrors",
                                "Cry Me a River",
                                "Rock Your Body",
                                "Summer Love",
                                "Losing My Way",
                                "Supplies",
                                "Take it From Here",
                                "Say Something",
                                "Tunnel Vision",
                                "Blue Ocean Floor"
                            ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column=0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column=1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='hot pink', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan=2)
        self.uzrasas1.grid(row = 0, columnspan=2)
        self.ladygaga.grid(row = 1, columnspan=2)
        self.beyonce.grid(row = 2, columnspan=2)
        self.britneysp.grid(row = 3, columnspan=2)
        self.chaguilera.grid(row = 4, columnspan=2)
        self.justint.grid(row = 5, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        self.uzdaryti_pop.grid(row = 9, columnspan=2)

    def picker(self):
        if self.dainu_boks.get() == "Bad Romance":
            webbrowser.open(('https://music.youtube.com/watch?v=fiRjp6y6QvI'), new = 2)
        if self.dainu_boks.get() == "Alejandro":
            webbrowser.open(('https://music.youtube.com/watch?v=DVEoBIZm0V8'), new = 2)
        if self.dainu_boks.get() == "Hold My Hand":
            webbrowser.open(('https://music.youtube.com/watch?v=nkzaMdWoqPU'), new = 2)
        if self.dainu_boks.get() == "Poker Face":
            webbrowser.open(('https://music.youtube.com/watch?v=GMAVUvb8Obs'), new = 2)
        if self.dainu_boks.get() == "Born This Way":
            webbrowser.open(('https://music.youtube.com/watch?v=fn8JP4rUP2I'), new = 2)
        if self.dainu_boks.get() == "Judas":
            webbrowser.open(('https://music.youtube.com/watch?v=9WfWnkVLwao'), new = 2)
        if self.dainu_boks.get() == "Paparazzi":
            webbrowser.open(('https://music.youtube.com/watch?v=V9qrpe2z9mE'), new = 2)
        if self.dainu_boks.get() == "John Wayne":
            webbrowser.open(('https://music.youtube.com/watch?v=7CkGrvx9Z3g'), new = 2)
        if self.dainu_boks.get() == "Alice":
            webbrowser.open(('https://music.youtube.com/watch?v=41CjTbmI9aQ'), new = 2)
        if self.dainu_boks.get() == "Love Game":
            webbrowser.open(('https://music.youtube.com/watch?v=cSRxQoeKbVM'), new = 2)
        if self.dainu_boks.get() == "Break My Soul":
            webbrowser.open(('https://music.youtube.com/watch?v=y6dw-v4BH-Y'), new = 2)
        if self.dainu_boks.get() == "Love on Top":
            webbrowser.open(('https://music.youtube.com/watch?v=n0R5uUEjjCk'), new = 2)
        if self.dainu_boks.get() == "Crazy Love":
            webbrowser.open(('https://music.youtube.com/watch?v=5BnF0_LksYI'), new = 2)
        if self.dainu_boks.get() == "Halo":
            webbrowser.open(('https://music.youtube.com/watch?v=VqQeT7wKqvs'), new = 2)
        if self.dainu_boks.get() == "Single Ladies":
            webbrowser.open(('https://music.youtube.com/watch?v=4z-bOdAdias'), new = 2)
        if self.dainu_boks.get() == "I was Here":
            webbrowser.open(('https://music.youtube.com/watch?v=hDb3jZfWpoA'), new = 2)
        if self.dainu_boks.get() == "Run the World":
            webbrowser.open(('https://music.youtube.com/watch?v=XC7eRmnfZ_A'), new = 2)
        if self.dainu_boks.get() == "All up in Your Mind":
            webbrowser.open(('https://music.youtube.com/watch?v=35zH9TppB4w'), new = 2)
        if self.dainu_boks.get() == "My Myself and I":
            webbrowser.open(('https://music.youtube.com/watch?v=MKSR7T7TQRA'), new = 2)
        if self.dainu_boks.get() == "Sorry":
            webbrowser.open(('https://music.youtube.com/watch?v=oKtAurJxlIg'), new = 2)
        if self.dainu_boks.get() == "Toxic":
            webbrowser.open(('https://music.youtube.com/watch?v=tVdr_JWmnsA'), new = 2)
        if self.dainu_boks.get() == "Baby One More Time":
            webbrowser.open(('https://music.youtube.com/watch?v=91Niv2q4gvc'), new = 2)
        if self.dainu_boks.get() == "Criminal":
            webbrowser.open(('https://music.youtube.com/watch?v=ux9-_2SN1h0'), new = 2)
        if self.dainu_boks.get() == "Work Bitch":
            webbrowser.open(('https://music.youtube.com/watch?v=2lLBLjn3FCI'), new = 2)
        if self.dainu_boks.get() == "Opps I did it Again":
            webbrowser.open(('https://music.youtube.com/watch?v=wsHbHR3Os6U'), new = 2)
        if self.dainu_boks.get() == "Bombastic Love":
            webbrowser.open(('https://music.youtube.com/watch?v=wNcZ6SSq49Q'), new = 2)
        if self.dainu_boks.get() == "Gimme More":
            webbrowser.open(('https://music.youtube.com/watch?v=_tnyHbiuQAc'), new = 2)
        if self.dainu_boks.get() == "Early Mornin'":
            webbrowser.open(('https://music.youtube.com/watch?v=gJn81ivTXZg'), new = 2)
        if self.dainu_boks.get() == "Sometimes":
            webbrowser.open(('https://music.youtube.com/watch?v=CbuLnJqUFLQ'), new = 2)
        if self.dainu_boks.get() == "Piece of Me":
            webbrowser.open(('https://music.youtube.com/watch?v=IyFizEee7vY'), new = 2)
        if self.dainu_boks.get() == "Dirrty":
            webbrowser.open(('https://music.youtube.com/watch?v=CdP2lLODk-A'), new = 2)
        if self.dainu_boks.get() == "Genie in a Bottle":
            webbrowser.open(('https://music.youtube.com/watch?v=yz4me7Vwr1w'), new = 2)
        if self.dainu_boks.get() == "Hurt":
            webbrowser.open(('https://music.youtube.com/watch?v=i6yMdwNeZ64'), new = 2)
        if self.dainu_boks.get() == "I turn to You":
            webbrowser.open(('https://music.youtube.com/watch?v=_jButDF_Rtw'), new = 2)
        if self.dainu_boks.get() == "Fighter":
            webbrowser.open(('https://music.youtube.com/watch?v=nsRls_7T8kE'), new = 2)
        if self.dainu_boks.get() == "Candyman":
            webbrowser.open(('https://music.youtube.com/watch?v=8vfY1Y369OE'), new = 2)
        if self.dainu_boks.get() == "Your Body":
            webbrowser.open(('https://music.youtube.com/watch?v=XaSWjJq99XM'), new = 2)
        if self.dainu_boks.get() == "Haunted Heart":
            webbrowser.open(('https://music.youtube.com/watch?v=MHW5oZREOmQ'), new = 2)
        if self.dainu_boks.get() == "Ven Conmingo":
            webbrowser.open(('https://music.youtube.com/watch?v=LeZf3btt_yY'), new = 2)
        if self.dainu_boks.get() == "Welcome":
            webbrowser.open(('https://music.youtube.com/watch?v=i-XQYvMn6AE'), new = 2)
        if self.dainu_boks.get() == "Mirrors":
            webbrowser.open(('https://music.youtube.com/watch?v=59nAgJZ5IoE'), new = 2)
        if self.dainu_boks.get() == "Cry Me a River":
            webbrowser.open(('https://music.youtube.com/watch?v=CIk45fEWBok'), new = 2)
        if self.dainu_boks.get() == "Rock Your Body":
            webbrowser.open(('https://music.youtube.com/watch?v=7EJbFg_LxjY'), new = 2)
        if self.dainu_boks.get() == "Summer Love":
            webbrowser.open(('https://music.youtube.com/watch?v=SpmCfl2UrPc'), new = 2)
        if self.dainu_boks.get() == "Losing My Way":
            webbrowser.open(('https://music.youtube.com/watch?v=D--EcySiMLQ'), new = 2)
        if self.dainu_boks.get() == "Supplies":
            webbrowser.open(('https://music.youtube.com/watch?v=cMIWOx66l4w'), new = 2)
        if self.dainu_boks.get() == "Take it From Here":
            webbrowser.open(('https://music.youtube.com/watch?v=RS7AjOdBDLk'), new = 2)
        if self.dainu_boks.get() == "Say Something":
            webbrowser.open(('https://music.youtube.com/watch?v=0ZXWM-8Oqwg'), new = 2)
        if self.dainu_boks.get() == "Tunnel Vision":
            webbrowser.open(('https://music.youtube.com/watch?v=Y9M0jZsNRMk'), new = 2)
        if self.dainu_boks.get() == "Blue Ocean Floor":
            webbrowser.open(('https://music.youtube.com/watch?v=mbP99oQSG_Q'), new = 2)
        

    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Lady Gaga":
            self.dainu_boks.config(value = self.lady_gaga_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Beyoncé":
            self.dainu_boks.config(value = self.beyonce_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Britney Spears":
            self.dainu_boks.config(value = self.britney_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Christina Aguilera":
            self.dainu_boks.config(value = self.aguilera_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Justin Timberlake":
            self.dainu_boks.config(value = self.timberlake_dainos)
            self.dainu_boks.current(0)


    def open_ladygaga(self):
        self.random_ladygaga = ['https://music.youtube.com/watch?v=fiRjp6y6QvI',
                                'https://music.youtube.com/watch?v=DVEoBIZm0V8',
                                'https://music.youtube.com/watch?v=nkzaMdWoqPU',
                                'https://music.youtube.com/watch?v=GMAVUvb8Obs',
                                'https://music.youtube.com/watch?v=fn8JP4rUP2I',
                                'https://music.youtube.com/watch?v=9WfWnkVLwao',
                                'https://music.youtube.com/watch?v=V9qrpe2z9mE',
                                'https://music.youtube.com/watch?v=7CkGrvx9Z3g',
                                'https://music.youtube.com/watch?v=41CjTbmI9aQ',
                                'https://music.youtube.com/watch?v=cSRxQoeKbVM'
                            ]
        webbrowser.open(choice(self.random_ladygaga), new = 2)

    def open_beyonce(self):
        self.random_beyonce = ['https://music.youtube.com/watch?v=y6dw-v4BH-Y',
                                'https://music.youtube.com/watch?v=n0R5uUEjjCk',
                                'https://music.youtube.com/watch?v=5BnF0_LksYI',
                                'https://music.youtube.com/watch?v=VqQeT7wKqvs',
                                'https://music.youtube.com/watch?v=4z-bOdAdias',
                                'https://music.youtube.com/watch?v=hDb3jZfWpoA',
                                'https://music.youtube.com/watch?v=XC7eRmnfZ_A',
                                'https://music.youtube.com/watch?v=35zH9TppB4w',
                                'https://music.youtube.com/watch?v=MKSR7T7TQRA',
                                'https://music.youtube.com/watch?v=oKtAurJxlIg'
                            ]
        webbrowser.open(choice(self.random_beyonce), new = 2)

    def open_britney(self):
        self.random_britney = ['https://music.youtube.com/watch?v=tVdr_JWmnsA',
                                'https://music.youtube.com/watch?v=91Niv2q4gvc',
                                'https://music.youtube.com/watch?v=ux9-_2SN1h0',
                                'https://music.youtube.com/watch?v=2lLBLjn3FCI',
                                'https://music.youtube.com/watch?v=wsHbHR3Os6U',
                                'https://music.youtube.com/watch?v=wNcZ6SSq49Q',
                                'https://music.youtube.com/watch?v=_tnyHbiuQAc',
                                'https://music.youtube.com/watch?v=gJn81ivTXZg',
                                'https://music.youtube.com/watch?v=CbuLnJqUFLQ',
                                'https://music.youtube.com/watch?v=IyFizEee7vY'
                            ]
        webbrowser.open(choice(self.random_britney), new = 2)

    def open_christina(self):
        self.random_christina = ['https://music.youtube.com/watch?v=CdP2lLODk-A',
                                'https://music.youtube.com/watch?v=yz4me7Vwr1w',
                                'https://music.youtube.com/watch?v=i6yMdwNeZ64',
                                'https://music.youtube.com/watch?v=_jButDF_Rtw',
                                'https://music.youtube.com/watch?v=nsRls_7T8kE',
                                'https://music.youtube.com/watch?v=8vfY1Y369OE',
                                'https://music.youtube.com/watch?v=XaSWjJq99XM',
                                'https://music.youtube.com/watch?v=MHW5oZREOmQ',
                                'https://music.youtube.com/watch?v=LeZf3btt_yY',
                                'https://music.youtube.com/watch?v=i-XQYvMn6AE'
                            ]
        webbrowser.open(choice(self.random_christina), new = 2)

    def open_justint(self):
        self.random_justint = ['https://music.youtube.com/watch?v=59nAgJZ5IoE',
                                'https://music.youtube.com/watch?v=CIk45fEWBok',
                                'https://music.youtube.com/watch?v=7EJbFg_LxjY',
                                'https://music.youtube.com/watch?v=SpmCfl2UrPc',
                                'https://music.youtube.com/watch?v=D--EcySiMLQ',
                                'https://music.youtube.com/watch?v=cMIWOx66l4w',
                                'https://music.youtube.com/watch?v=RS7AjOdBDLk',
                                'https://music.youtube.com/watch?v=0ZXWM-8Oqwg',
                                'https://music.youtube.com/watch?v=Y9M0jZsNRMk',
                                'https://music.youtube.com/watch?v=mbP99oQSG_Q'
                            ]
        webbrowser.open(choice(self.random_justint), new = 2)

    def uzdaryti(self):
        self.master.destroy()

class VidinisDisco:
    def __init__(self, master):
        self.master = master
        self.abba = tk.Button(self.master, text = "Abba", width = 15, command = self.open_abba, highlightbackground='cyan')
        self.beegees = tk.Button(self.master, text = "Bee Gees", width = 15, command = self.open_beegees, highlightbackground='cyan')
        self.sandra = tk.Button(self.master, text = "Sandra", width = 15, command = self.open_sandra, highlightbackground='cyan')
        self.boneym = tk.Button(self.master, text = "Boney M.", width = 15, command = self.open_boneym, highlightbackground='cyan')
        self.dsummer = tk.Button(self.master, text = "Donna Summer", width = 15, command = self.open_dsummer, highlightbackground='cyan')
        self.uzdaryti_disco = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground='cyan')
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = 'cyan')
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = 'cyan')
        self.atlikeju_sarasas = ["Abba", "Bee Gees", "Sandra", "Boney M.", "Donna Summer"]
        self.abba_dainos = ["Gimme Gimme",
                            "Dancing Queen",
                            "Mama Mia",
                            "Waterloo",
                            "SOS",
                            "Lay All Your Love On Me",
                            "Voulez Vous",
                            "Money Money",
                            "Take a Chance On Me",
                            "Fernando"
                        ]
        self.bee_gees_dainos = ["Stayin' Alive",
                                "How Deep is Your Love",
                                "Words",
                                "I started a Joke",
                                "Too Much Heaven",
                                "You Should Be Dancing",
                                "Night Fever",
                                "Secret Love",
                                "My World",
                                "Jive Talkin'"
                            ]
        self.sandra_dainos = ["Maria Magdelena",
                            "Heaven Can Wait",
                            "Around My Heart",
                            "Little Girl",
                            "Such a Shame",
                            "In the Heat of The Night",
                            "We Will Be Together",
                            "You and I",
                            "You'll be Mine",
                            "Hi! Hi! Hi!"
                        ]
        self.boneym_dainos = ["Daddy Cool",
                            "Rasputin",
                            "Sunny",
                            "Rivers of Babylon",
                            "Ma Baker",
                            "Brown Girl in the Ring",
                            "Jimmy",
                            "Heart of Gold",
                            "Happy Song",
                            "Hands Up"
                        ]
        self.donnas_dainos = ["Hot Stuff",
                            "I Feel Love",
                            "Last Dance",
                            "She Works Hard for the Money",
                            "Breakaway",
                            "Dim All the Lights",
                            "Tokyo",
                            "Walk Away",
                            "Rumour Has It",
                            "Protection"
                        ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 7, column=0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 7, column=1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='cyan', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 8, columnspan=2)
        self.uzrasas1.grid(row = 0, columnspan=2)
        self.abba.grid(row = 1, columnspan=2)
        self.beegees.grid(row = 2, columnspan=2)
        self.sandra.grid(row = 3, columnspan=2)
        self.boneym.grid(row = 4, columnspan=2)
        self.dsummer.grid(row = 5, columnspan=2)
        self.uzrasas2.grid(row = 6, columnspan=2)
        self.uzdaryti_disco.grid(row = 9, columnspan=2)
    
    def picker(self):
        if self.dainu_boks.get() == "Gimme Gimme":
            webbrowser.open(('https://music.youtube.com/watch?v=pa2j0Bh83ms'), new = 2)
        if self.dainu_boks.get() == "Dancing Queen":
            webbrowser.open(('https://music.youtube.com/watch?v=YkLLcIKhJ64'), new = 2)
        if self.dainu_boks.get() == "Mama Mia":
            webbrowser.open(('https://music.youtube.com/watch?v=KMViJKmAV4M'), new = 2)
        if self.dainu_boks.get() == "Waterloo":
            webbrowser.open(('https://music.youtube.com/watch?v=9y-8ZiAJiQo'), new = 2)
        if self.dainu_boks.get() == "SOS":
            webbrowser.open(('https://music.youtube.com/watch?v=CxMcD8QHVag'), new = 2)
        if self.dainu_boks.get() == "Lay All Your Love On Me":
            webbrowser.open(('https://music.youtube.com/watch?v=5mHzaIehRTE'), new = 2)
        if self.dainu_boks.get() == "Voulez Vous":
            webbrowser.open(('https://music.youtube.com/watch?v=0X2mn7Sk9lQ'), new = 2)
        if self.dainu_boks.get() == "Money Money":
            webbrowser.open(('https://music.youtube.com/watch?v=1LPNuFkteI8'), new = 2)
        if self.dainu_boks.get() == "Take a Chance On Me":
            webbrowser.open(('https://music.youtube.com/watch?v=DkkQ8dCPiwA'), new = 2)
        if self.dainu_boks.get() == "Fernando":
            webbrowser.open(('https://music.youtube.com/watch?v=b-U3-Sla8GM'), new = 2)
        if self.dainu_boks.get() == "Stayin' Alive":
            webbrowser.open(('https://music.youtube.com/watch?v=W_dDNNEdIJg'), new = 2)
        if self.dainu_boks.get() == "How Deep is Your Love":
            webbrowser.open(('https://music.youtube.com/watch?v=lQkB4i0KQa8'), new = 2)
        if self.dainu_boks.get() == "Words":
            webbrowser.open(('https://music.youtube.com/watch?v=UmoAMZg8MvI'), new = 2)
        if self.dainu_boks.get() == "I started a Joke":
            webbrowser.open(('https://music.youtube.com/watch?v=4ZWKR2zJESk'), new = 2)
        if self.dainu_boks.get() == "Too Much Heaven":
            webbrowser.open(('https://music.youtube.com/watch?v=gdqVP35IQqQ'), new = 2)
        if self.dainu_boks.get() == "You Should Be Dancing":
            webbrowser.open(('https://music.youtube.com/watch?v=1sqE6P3XyiQ'), new = 2)
        if self.dainu_boks.get() == "Night Fever":
            webbrowser.open(('https://music.youtube.com/watch?v=Lc8uj8eId7E'), new = 2)
        if self.dainu_boks.get() == "Secret Love":
            webbrowser.open(('https://music.youtube.com/watch?v=LQviz__oHug'), new = 2)
        if self.dainu_boks.get() == "My World":
            webbrowser.open(('https://music.youtube.com/watch?v=-t7PTruoz6s'), new = 2)
        if self.dainu_boks.get() == "Jive Talkin'":
            webbrowser.open(('https://music.youtube.com/watch?v=SYVT-FMeFts'), new = 2)
        if self.dainu_boks.get() == "Maria Magdelena":
            webbrowser.open(('https://music.youtube.com/watch?v=NP4LZZGYI5E'), new = 2)
        if self.dainu_boks.get() == "Heaven Can Wait":
            webbrowser.open(('https://music.youtube.com/watch?v=pKpS19CThyQ'), new = 2)
        if self.dainu_boks.get() == "Around My Heart":
            webbrowser.open(('https://music.youtube.com/watch?v=F8ZLbdbp75A'), new = 2)
        if self.dainu_boks.get() == "Little Girl":
            webbrowser.open(('https://music.youtube.com/watch?v=jhvVx9-Yusk'), new = 2)
        if self.dainu_boks.get() == "Such a Shame":
            webbrowser.open(('https://music.youtube.com/watch?v=dencYmYKkeY'), new = 2)
        if self.dainu_boks.get() == "In the Heat of The Night":
            webbrowser.open(('https://music.youtube.com/watch?v=HSoTCQXJsDQ'), new = 2)
        if self.dainu_boks.get() == "We Will Be Together":
            webbrowser.open(('https://music.youtube.com/watch?v=-jnpbEbSugQ'), new = 2)
        if self.dainu_boks.get() == "You and I":
            webbrowser.open(('https://music.youtube.com/watch?v=9oNAC8hFSl0'), new = 2)
        if self.dainu_boks.get() == "You'll be Mine":
            webbrowser.open(('https://music.youtube.com/watch?v=bIY4cSzlSLk'), new = 2)
        if self.dainu_boks.get() == "Hi! Hi! Hi!":
            webbrowser.open(('https://music.youtube.com/watch?v=iBZedwqwpMo'), new = 2)
        if self.dainu_boks.get() == "Daddy Cool":
            webbrowser.open(('https://music.youtube.com/watch?v=iQEpTa3VqLU'), new = 2)
        if self.dainu_boks.get() == "Rasputin":
            webbrowser.open(('https://music.youtube.com/watch?v=5Z0dxsFmX7c'), new = 2)
        if self.dainu_boks.get() == "Sunny":
            webbrowser.open(('https://music.youtube.com/watch?v=bQ7k2YRODT4'), new = 2)
        if self.dainu_boks.get() == "Rivers of Babylon":
            webbrowser.open(('https://music.youtube.com/watch?v=gr8jSYC03gQ'), new = 2)
        if self.dainu_boks.get() == "Ma Baker":
            webbrowser.open(('https://music.youtube.com/watch?v=2GogVZiVFxM'), new = 2)
        if self.dainu_boks.get() == "Brown Girl in the Ring":
            webbrowser.open(('https://music.youtube.com/watch?v=2VKeyJEouv4'), new = 2)
        if self.dainu_boks.get() == "Jimmy":
            webbrowser.open(('https://music.youtube.com/watch?v=ix4VWyLJv8Y'), new = 2)
        if self.dainu_boks.get() == "Heart of Gold":
            webbrowser.open(('https://music.youtube.com/watch?v=nCyeIoajBl8'), new = 2)
        if self.dainu_boks.get() == "Happy Song":
            webbrowser.open(('https://music.youtube.com/watch?v=mJU3K16AiHs'), new = 2)
        if self.dainu_boks.get() == "Hands Up":
            webbrowser.open(('https://music.youtube.com/watch?v=dlaGYG4iOas'), new = 2)
        if self.dainu_boks.get() == "Hot Stuff":
            webbrowser.open(('https://music.youtube.com/watch?v=nYMeJSehCe4'), new = 2)
        if self.dainu_boks.get() == "I Feel Love":
            webbrowser.open(('https://music.youtube.com/watch?v=nTNcCKq6V2c'), new = 2)
        if self.dainu_boks.get() == "Last Dance":
            webbrowser.open(('https://music.youtube.com/watch?v=561fy1vqIo8'), new = 2)
        if self.dainu_boks.get() == "She Works Hard for the Money":
            webbrowser.open(('https://music.youtube.com/watch?v=tuUEpbGVV2Y'), new = 2)
        if self.dainu_boks.get() == "Breakaway":
            webbrowser.open(('https://music.youtube.com/watch?v=wOf9yTO2vKI'), new = 2)
        if self.dainu_boks.get() == "Dim All the Lights":
            webbrowser.open(('https://music.youtube.com/watch?v=zqMXVxyFmQg'), new = 2)
        if self.dainu_boks.get() == "Tokyo":
            webbrowser.open(('https://music.youtube.com/watch?v=mNEySGzN3Vs'), new = 2)
        if self.dainu_boks.get() == "Walk Away":
            webbrowser.open(('https://music.youtube.com/watch?v=xeMK3J6DIM0'), new = 2)
        if self.dainu_boks.get() == "Rumour Has It":
            webbrowser.open(('https://music.youtube.com/watch?v=mi-QzaZnGjo'), new = 2)
        if self.dainu_boks.get() == "Protection":
            webbrowser.open(('https://music.youtube.com/watch?v=Hs5FrKcMZs0'), new = 2)

        

    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Abba":
            self.dainu_boks.config(value = self.abba_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Bee Gees":
            self.dainu_boks.config(value = self.bee_gees_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Sandra":
            self.dainu_boks.config(value = self.sandra_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Boney M.":
            self.dainu_boks.config(value = self.boneym_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Donna Summer":
            self.dainu_boks.config(value = self.donnas_dainos)
            self.dainu_boks.current(0)

    def open_abba(self):
        self.random_abba = ['https://music.youtube.com/watch?v=pa2j0Bh83ms',
                            'https://music.youtube.com/watch?v=YkLLcIKhJ64',
                            'https://music.youtube.com/watch?v=KMViJKmAV4M',
                            'https://music.youtube.com/watch?v=9y-8ZiAJiQo',
                            'https://music.youtube.com/watch?v=CxMcD8QHVag',
                            'https://music.youtube.com/watch?v=5mHzaIehRTE',
                            'https://music.youtube.com/watch?v=0X2mn7Sk9lQ',
                            'https://music.youtube.com/watch?v=1LPNuFkteI8',
                            'https://music.youtube.com/watch?v=DkkQ8dCPiwA',
                            'https://music.youtube.com/watch?v=b-U3-Sla8GM'
                        ]
        webbrowser.open(choice(self.random_abba), new = 2)

    def open_beegees(self):
        self.random_bee_gees = ['https://music.youtube.com/watch?v=W_dDNNEdIJg',
                                'https://music.youtube.com/watch?v=lQkB4i0KQa8',
                                'https://music.youtube.com/watch?v=UmoAMZg8MvI',
                                'https://music.youtube.com/watch?v=4ZWKR2zJESk',
                                'https://music.youtube.com/watch?v=gdqVP35IQqQ',
                                'https://music.youtube.com/watch?v=1sqE6P3XyiQ',
                                'https://music.youtube.com/watch?v=Lc8uj8eId7E',
                                'https://music.youtube.com/watch?v=LQviz__oHug',
                                'https://music.youtube.com/watch?v=-t7PTruoz6s',
                                'https://music.youtube.com/watch?v=SYVT-FMeFts'
                            ]
        webbrowser.open(choice(self.random_bee_gees), new = 2)

    def open_sandra(self):
        self.random_sandra = ['https://music.youtube.com/watch?v=NP4LZZGYI5E',
                            'https://music.youtube.com/watch?v=pKpS19CThyQ',
                            'https://music.youtube.com/watch?v=F8ZLbdbp75A',
                            'https://music.youtube.com/watch?v=jhvVx9-Yusk',
                            'https://music.youtube.com/watch?v=dencYmYKkeY',
                            'https://music.youtube.com/watch?v=HSoTCQXJsDQ',
                            'https://music.youtube.com/watch?v=-jnpbEbSugQ',
                            'https://music.youtube.com/watch?v=9oNAC8hFSl0',
                            'https://music.youtube.com/watch?v=bIY4cSzlSLk',
                            'https://music.youtube.com/watch?v=iBZedwqwpMo'
                            ]
        webbrowser.open(choice(self.random_sandra), new = 2)

    def open_boneym(self):
        self.random_boneym = ['https://music.youtube.com/watch?v=iQEpTa3VqLU',
                            'https://music.youtube.com/watch?v=5Z0dxsFmX7c',
                            'https://music.youtube.com/watch?v=bQ7k2YRODT4',
                            'https://music.youtube.com/watch?v=gr8jSYC03gQ',
                            'https://music.youtube.com/watch?v=2GogVZiVFxM',
                            'https://music.youtube.com/watch?v=2VKeyJEouv4',
                            'https://music.youtube.com/watch?v=ix4VWyLJv8Y',
                            'https://music.youtube.com/watch?v=nCyeIoajBl8',
                            'https://music.youtube.com/watch?v=mJU3K16AiHs',
                            'https://music.youtube.com/watch?v=dlaGYG4iOas'
                        ]
        webbrowser.open(choice(self.random_boneym), new = 2)

    def open_dsummer(self):
        self.random_dsummer = ['https://music.youtube.com/watch?v=nYMeJSehCe4',
                                'https://music.youtube.com/watch?v=nTNcCKq6V2c',
                                'https://music.youtube.com/watch?v=561fy1vqIo8',
                                'https://music.youtube.com/watch?v=tuUEpbGVV2Y',
                                'https://music.youtube.com/watch?v=wOf9yTO2vKI',
                                'https://music.youtube.com/watch?v=zqMXVxyFmQg',
                                'https://music.youtube.com/watch?v=mNEySGzN3Vs',
                                'https://music.youtube.com/watch?v=xeMK3J6DIM0',
                                'https://music.youtube.com/watch?v=mi-QzaZnGjo',
                                'https://music.youtube.com/watch?v=Hs5FrKcMZs0'
                            ]
        webbrowser.open(choice(self.random_dsummer), new = 2)

    def uzdaryti(self):
        self.master.destroy()

class VidinisJazz:
    def __init__(self, master):
        self.master = master
        self.candyd = tk.Button(self.master, text = "Candy Dulfer", width = 15, command = self.open_candy_duler, highlightbackground = "DarkGoldenrod1")
        self.amstrong = tk.Button(self.master, text = "Louis Amstrong", width = 15, command = self.open_amstrong, highlightbackground = "DarkGoldenrod1")
        self.fitzgerald = tk.Button(self.master, text = "Ella Fitzgerald", width = 15, command = self.open_fitzgerald, highlightbackground = "DarkGoldenrod1")
        self.countb = tk.Button(self.master, text = "Count Basie", width = 15, command = self.open_countb, highlightbackground = "DarkGoldenrod1")
        self.ninasimone = tk.Button(self.master, text = "Nina Simone", width = 15, command = self.open_nina_simone, highlightbackground = "DarkGoldenrod1")
        self.uzdaryti_jazz = tk.Button(self.master, text = "\u2573 Uždaryti", width = 25, command = self.uzdaryti, highlightbackground = "DarkGoldenrod1")
        self.uzrasas1 = Label(self.master, text = "Išsirinkite atlikėją ir\njo dainą parinksime atsitiktinai.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "DarkGoldenrod1")
        self.uzrasas2 = Label(self.master, text = "Arba išsirinkite atlikėją\n ir dainą, kurią norite klausyti.", font = ('Courier New', 15, "bold"), fg = 'white', bg = "DarkGoldenrod1")
        self.atlikeju_sarasas = ["Candy Dulfer", "Louis Amstrong", "Ella Fitzgerald", "Count Basie", "Nina Simone"]
        self.candy_dainos = ["Lily Was Here",
                            "Smooth",
                            "If I ruled the World",
                            "For the Love of You",
                            "Promises",
                            "Music=Love",
                            "Candy",
                            "Right in My Soul",
                            "D.I.S.C.O",
                            "Wish You Were Here"
                        ]
        self.louis_dainos = ["What a Wonderful World",
                            "When You Were Smiling",
                            "Mack the Knife",
                            "St. James Infirmary",
                            "I Ain't Got Nobody",
                            "Hello Brother",
                            "Jeepers Creepers",
                            "Gonne Fishin'",
                            "Bibbidi-Bobbidi-Boo",
                            "Hello Dolly"
                        ]
        self.ella_dainos = ["Cry Me a River",
                            "All of Me",
                            "Summertime",
                            "Misty",
                            "Dream a Little Dream of Me",
                            "Cheek to Cheek",
                            "I can't Get Started",
                            "Angel Eyes",
                            "Like Someone in Love",
                            "Always"
                        ]
        self.basie_dainos = ["Lady Be Good",
                            "Straight Ahead",
                            "Corner Pocket",
                            "Teddy the Toad",
                            "Hay Burner",
                            "Moten Swing",
                            "Strike Up the Band",
                            "Lonely Street",
                            "Switch in Time",
                            "Lil' Darlin"
                        ]
        self.ninas_dainos = ["Feeling Good",
                            "I Put a Spell on You",
                            "Sinnerman",
                            "My Way",
                            "Blues for Mama",
                            "Take Me to the Water",
                            "Strange Fruit",
                            "I am Blessed",
                            "Cherish",
                            "Blackbird"
                        ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.grid(row = 8, column=0)
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.grid(row = 8, column=1)

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='DarkGoldenrod1', command = self.picker)
        self.pasirinkti_mygtukas.grid(row = 9, columnspan=2)
        self.uzrasas1.grid(row = 1, columnspan=2)
        self.candyd.grid(row = 2, columnspan=2)
        self.amstrong.grid(row = 3, columnspan=2)
        self.fitzgerald.grid(row = 4, columnspan=2)
        self.countb.grid(row = 5, columnspan=2)
        self.ninasimone.grid(row = 6, columnspan=2)
        self.uzrasas2.grid(row = 7, columnspan=2)
        self.uzdaryti_jazz.grid(row = 10, columnspan=2)

    def picker(self):
        if self.dainu_boks.get() == "Blackbird":
            webbrowser.open(('https://music.youtube.com/watch?v=sXJTMKv3ZmA'), new = 2)
        if self.dainu_boks.get() == "Feeling Good":
            webbrowser.open(('https://music.youtube.com/watch?v=BNMKGYiJpvg'), new = 2)
        if self.dainu_boks.get() == "I Put a Spell on You":
            webbrowser.open(('https://music.youtube.com/watch?v=qgn-dnCkOTw'), new = 2)
        if self.dainu_boks.get() == "Sinnerman":
            webbrowser.open(('https://music.youtube.com/watch?v=3KyUicgOm74'), new = 2)
        if self.dainu_boks.get() == "My Way":
            webbrowser.open(('https://music.youtube.com/watch?v=gwcz2BwEdqs'), new = 2)
        if self.dainu_boks.get() == "Blues for Mama":
            webbrowser.open(('https://music.youtube.com/watch?v=n2rFOEGctUo'), new = 2)
        if self.dainu_boks.get() == "Take Me to the Water":
            webbrowser.open(('https://music.youtube.com/watch?v=AJjmX1zKzPs'), new = 2)
        if self.dainu_boks.get() == "Strange Fruit":
            webbrowser.open(('https://music.youtube.com/watch?v=33dgafi_Gv8'), new = 2)
        if self.dainu_boks.get() == "I am Blessed":
            webbrowser.open(('https://music.youtube.com/watch?v=llNopGK8xL4'), new = 2)
        if self.dainu_boks.get() == "Cherish":
            webbrowser.open(('https://music.youtube.com/watch?v=08NnLiWOlQo'), new = 2)
        if self.dainu_boks.get() == "Lily Was Here":
            webbrowser.open(('https://music.youtube.com/watch?v=SS0HmeaLBOg'), new = 2)
        if self.dainu_boks.get() == "Smooth":
            webbrowser.open(('https://music.youtube.com/watch?v=QtVbG_rPLWc'), new = 2)
        if self.dainu_boks.get() == "If I ruled the World":
            webbrowser.open(('https://music.youtube.com/watch?v=Bn24CZEkkdk'), new = 2)
        if self.dainu_boks.get() == "For the Love of You":
            webbrowser.open(('https://music.youtube.com/watch?v=j6c4YwN-0Uo'), new = 2)
        if self.dainu_boks.get() == "Promises":
            webbrowser.open(('https://music.youtube.com/watch?v=lnmE8is8fdA'), new = 2)
        if self.dainu_boks.get() == "Music=Love":
            webbrowser.open(('https://music.youtube.com/watch?v=HA7uR0iSkaw'), new = 2)
        if self.dainu_boks.get() == "Candy":
            webbrowser.open(('https://music.youtube.com/watch?v=0k8TBfvrXVk'), new = 2)
        if self.dainu_boks.get() == "Right in My Soul":
            webbrowser.open(('https://music.youtube.com/watch?v=Zclro7ercfE'), new = 2)
        if self.dainu_boks.get() == "D.I.S.C.O":
            webbrowser.open(('https://music.youtube.com/watch?v=ZwSH2Y0JN2Q'), new = 2)
        if self.dainu_boks.get() == "Wish You Were Here":
            webbrowser.open(('https://music.youtube.com/watch?v=7W6sXxkeUQw'), new = 2)
        if self.dainu_boks.get() == "What a Wonderful World":
            webbrowser.open(('https://music.youtube.com/watch?v=e1FN047_LT0'), new = 2)
        if self.dainu_boks.get() == "When You Were Smiling":
            webbrowser.open(('https://music.youtube.com/watch?v=jNp7dCmbNXA'), new = 2)
        if self.dainu_boks.get() == "Mack the Knife":
            webbrowser.open(('https://music.youtube.com/watch?v=ADQFDonofRw'), new = 2)
        if self.dainu_boks.get() == "St. James Infirmary":
            webbrowser.open(('https://music.youtube.com/watch?v=BMAD00G0oz8'), new = 2)
        if self.dainu_boks.get() == "I Ain't Got Nobody":
            webbrowser.open(('https://music.youtube.com/watch?v=LCLrnxUoF4o'), new = 2)
        if self.dainu_boks.get() == "Hello Brother":
            webbrowser.open(('https://music.youtube.com/watch?v=brsPG22tE9U'), new = 2)
        if self.dainu_boks.get() == "Jeepers Creepers":
            webbrowser.open(('https://music.youtube.com/watch?v=LMsBKsSIoIo'), new = 2)
        if self.dainu_boks.get() == "Gonne Fishin'":
            webbrowser.open(('https://music.youtube.com/watch?v=UQuU999MURo'), new = 2)
        if self.dainu_boks.get() == "Bibbidi-Bobbidi-Boo":
            webbrowser.open(('https://music.youtube.com/watch?v=RxflhrRcyLk'), new = 2)
        if self.dainu_boks.get() == "Hello Dolly":
            webbrowser.open(('https://music.youtube.com/watch?v=YCM0APgpdZc'), new = 2)
        if self.dainu_boks.get() == "Lady Be Good":
            webbrowser.open(('https://music.youtube.com/watch?v=iHfwUwmX3V4'), new = 2)
        if self.dainu_boks.get() == "Straight Ahead":
            webbrowser.open(('https://music.youtube.com/watch?v=fm8uHT-BJP4'), new = 2)
        if self.dainu_boks.get() == "Corner Pocket":
            webbrowser.open(('https://music.youtube.com/watch?v=bTcmPGdDecw'), new = 2)
        if self.dainu_boks.get() == "Teddy the Toad":
            webbrowser.open(('https://music.youtube.com/watch?v=hL0PVQi-syk'), new = 2)
        if self.dainu_boks.get() == "Hay Burner":
            webbrowser.open(('https://music.youtube.com/watch?v=_Jl9IOqZb7U'), new = 2)
        if self.dainu_boks.get() == "Moten Swing":
            webbrowser.open(('https://music.youtube.com/watch?v=MxYWsWpjCOY'), new = 2)
        if self.dainu_boks.get() == "Strike Up the Band":
            webbrowser.open(('https://music.youtube.com/watch?v=03cLoi0bfo4'), new = 2)
        if self.dainu_boks.get() == "Lonely Street":
            webbrowser.open(('https://music.youtube.com/watch?v=I2l4qBuFWgE'), new = 2)
        if self.dainu_boks.get() == "Switch in Time":
            webbrowser.open(('https://music.youtube.com/watch?v=BSe0vKkRCrs'), new = 2)
        if self.dainu_boks.get() == "Lil' Darlin":
            webbrowser.open(('https://music.youtube.com/watch?v=nqn4nyZz0to'), new = 2)
        if self.dainu_boks.get() == "Cry Me a River":
            webbrowser.open(('https://music.youtube.com/watch?v=wSw8KaZIzYg'), new = 2)
        if self.dainu_boks.get() == "All of Me":
            webbrowser.open(('https://music.youtube.com/watch?v=Sr_EX9Ppfjw'), new = 2)
        if self.dainu_boks.get() == "Summertime":
            webbrowser.open(('https://music.youtube.com/watch?v=VZRgiuAXRAs'), new = 2)
        if self.dainu_boks.get() == "Misty":
            webbrowser.open(('https://music.youtube.com/watch?v=jy5x7bDYd4o'), new = 2)
        if self.dainu_boks.get() == "Dream a Little Dream of Me":
            webbrowser.open(('https://music.youtube.com/watch?v=vAd1lt5ANoA'), new = 2)
        if self.dainu_boks.get() == "Cheek to Cheek":
            webbrowser.open(('https://music.youtube.com/watch?v=lFiGn5lpahc'), new = 2)
        if self.dainu_boks.get() == "I can't Get Started":
            webbrowser.open(('https://music.youtube.com/watch?v=DFwWoXTMKrw'), new = 2)
        if self.dainu_boks.get() == "Angel Eyes":
            webbrowser.open(('https://music.youtube.com/watch?v=VBz1rXoSP9o'), new = 2)
        if self.dainu_boks.get() == "Like Someone in Love":
            webbrowser.open(('https://music.youtube.com/watch?v=ICOWB8X3H3M'), new = 2)
        if self.dainu_boks.get() == "Always":
            webbrowser.open(('https://music.youtube.com/watch?v=-c7yjsTHGF0'), new = 2)
        
        


    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Candy Dulfer":
            self.dainu_boks.config(value = self.candy_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Louis Amstrong":
            self.dainu_boks.config(value = self.louis_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Ella Fitzgerald":
            self.dainu_boks.config(value = self.ella_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Count Basie":
            self.dainu_boks.config(value = self.basie_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Nina Simone":
            self.dainu_boks.config(value = self.ninas_dainos)
            self.dainu_boks.current(0)

    
    def open_candy_duler(self):
        self.random_candy_dulfer = ['https://music.youtube.com/watch?v=SS0HmeaLBOg',
                                    'https://music.youtube.com/watch?v=QtVbG_rPLWc',
                                    'https://music.youtube.com/watch?v=Bn24CZEkkdk',
                                    'https://music.youtube.com/watch?v=j6c4YwN-0Uo',
                                    'https://music.youtube.com/watch?v=lnmE8is8fdA',
                                    'https://music.youtube.com/watch?v=HA7uR0iSkaw',
                                    'https://music.youtube.com/watch?v=0k8TBfvrXVk',
                                    'https://music.youtube.com/watch?v=Zclro7ercfE',
                                    'https://music.youtube.com/watch?v=ZwSH2Y0JN2Q',
                                    'https://music.youtube.com/watch?v=7W6sXxkeUQw'
                                ]
        webbrowser.open(choice(self.random_candy_dulfer), new = 2)

    def open_amstrong(self):
        self.random_amstrong = ['https://music.youtube.com/watch?v=e1FN047_LT0',
                                'https://music.youtube.com/watch?v=jNp7dCmbNXA',
                                'https://music.youtube.com/watch?v=ADQFDonofRw',
                                'https://music.youtube.com/watch?v=BMAD00G0oz8',
                                'https://music.youtube.com/watch?v=LCLrnxUoF4o',
                                'https://music.youtube.com/watch?v=brsPG22tE9U',
                                'https://music.youtube.com/watch?v=LMsBKsSIoIo',
                                'https://music.youtube.com/watch?v=UQuU999MURo',
                                'https://music.youtube.com/watch?v=RxflhrRcyLk',
                                'https://music.youtube.com/watch?v=YCM0APgpdZc'
                            ]
        webbrowser.open(choice(self.random_amstrong), new = 2)

    def open_fitzgerald(self):
        self.random_fitzgerald = ['https://music.youtube.com/watch?v=wSw8KaZIzYg',
                                'https://music.youtube.com/watch?v=Sr_EX9Ppfjw',
                                'https://music.youtube.com/watch?v=VZRgiuAXRAs',
                                'https://music.youtube.com/watch?v=jy5x7bDYd4o',
                                'https://music.youtube.com/watch?v=vAd1lt5ANoA',
                                'https://music.youtube.com/watch?v=lFiGn5lpahc',
                                'https://music.youtube.com/watch?v=DFwWoXTMKrw',
                                'https://music.youtube.com/watch?v=VBz1rXoSP9o',
                                'https://music.youtube.com/watch?v=ICOWB8X3H3M',
                                'https://music.youtube.com/watch?v=-c7yjsTHGF0'
                            ]
        webbrowser.open(choice(self.random_fitzgerald), new = 2)

    def open_countb(self):
        self.random_countb = ['https://music.youtube.com/watch?v=iHfwUwmX3V4',
                            'https://music.youtube.com/watch?v=fm8uHT-BJP4',
                            'https://music.youtube.com/watch?v=bTcmPGdDecw',
                            'https://music.youtube.com/watch?v=hL0PVQi-syk',
                            'https://music.youtube.com/watch?v=_Jl9IOqZb7U',
                            'https://music.youtube.com/watch?v=MxYWsWpjCOY',
                            'https://music.youtube.com/watch?v=03cLoi0bfo4',
                            'https://music.youtube.com/watch?v=I2l4qBuFWgE',
                            'https://music.youtube.com/watch?v=BSe0vKkRCrs',
                            'https://music.youtube.com/watch?v=nqn4nyZz0to'
                        ]
        webbrowser.open(choice(self.random_countb), new = 2)

    def open_nina_simone(self):
        self.random_nina_simone = ['https://music.youtube.com/watch?v=BNMKGYiJpvg',
                                    'https://music.youtube.com/watch?v=qgn-dnCkOTw',
                                    'https://music.youtube.com/watch?v=3KyUicgOm74',
                                    'https://music.youtube.com/watch?v=gwcz2BwEdqs',
                                    'https://music.youtube.com/watch?v=n2rFOEGctUo',
                                    'https://music.youtube.com/watch?v=AJjmX1zKzPs',
                                    'https://music.youtube.com/watch?v=33dgafi_Gv8',
                                    'https://music.youtube.com/watch?v=llNopGK8xL4',
                                    'https://music.youtube.com/watch?v=08NnLiWOlQo',
                                    'https://music.youtube.com/watch?v=sXJTMKv3ZmA'
                                ]
        webbrowser.open(choice(self.random_nina_simone), new = 2)
    
    def uzdaryti(self):
        self.master.destroy()

class VidinisBlues:
    def __init__(self, master):
        self.master = master
        self.mightysam = tk.Button(self.master, text = "Mighty Sam McClain", width = 15, command = self.open_mightysam, highlightbackground = "burlywood4")
        self.myers = tk.Button(self.master, text = "Sam Myers", width = 15, command = self.open_myers, highlightbackground = "burlywood4")
        self.cummings = tk.Button(self.master, text = "Albert Cummings", width = 15, command = self.open_cummings, highlightbackground = "burlywood4")
        self.rodgers = tk.Button(self.master, text = "Mighty Mo Rodgers", width = 15, command = self.open_rodgers, highlightbackground = "burlywood4")
        self.smokehouse = tk.Button(self.master, text = "Smokehouse", width = 15, command = self.open_smokehouse, highlightbackground = "burlywood4")
        self.uzdaryti_blues = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground = "burlywood4")
        self.atlikeju_sarasas = ["Mighty Sam McClain", "Sam Myers", "Albert Cummings", "Mighty Mo Rodgers", "Smokehouse"]
        self.mcclain_dainos = ["When The Hurt is Over",
                                "Don't Worry About Me",
                                "I am so Lonely",
                                "I am Tired of These Blues",
                                "Where You Been So Long",
                                "If You Could See",
                                "Where Is the Love",
                                "A Soul That Has Been Abused",
                                "Other Side of the Tracks",
                                "If It Wasn't for Blues"
                            ]
        self.myers_dainos = ["I Got the Blues",
                            "Let You Slowly Bring Me Down",
                            "I am Tired of Your Jive",
                            "Burning Fire",
                            "My Daily Wish",
                            "Coming from the Old School",
                            "Burning Fire",
                            "Sad and Lonesome",
                            "Sleeping in the Ground",
                            "Ninety Nine"
                        ]
        self.cummings_dainos = ["Workin' Man Blues",
                                "Meet the Man",
                                "Need Somebody",
                                "Lonely Bed",
                                "Little Bird",
                                "Rumors",
                                "Too Old To Grow Up",
                                "So Strong",
                                "Last Call",
                                "Get Out of Here"
                            ]
        self.rodgers_dainos = ["Picasso Blues",
                                "Black Paris Blues",
                                "Blues is a Woman Woe is a Man",
                                "My Blues, My Woman and My Car",
                                "Black Coffee and Cigarettes",
                                "The Boy Who Stole the Blues",
                                "Shame",
                                "No Regrets",
                                "Tomorrow Isn't Promised",
                                "Cadillac Ranch"
                            ]
        self.smokehouse_dainos = ["Cadillac in the Swamps",
                                "Haints in my House",
                                "Go Down Moses",
                                "Hoodoo You?",
                                "Creepin' Blues",
                                "Nice 'N' Round",
                                "Crack Smokin' Blues",
                                "Bisquit Roller",
                                "Martin Luther \"The King\"",
                                "American Dream"
                            ]
        self.atlikeju_boks = ttk.Combobox(self.master, value = self.atlikeju_sarasas)
        self.atlikeju_boks.current(0)
        self.atlikeju_boks.pack()
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.pack()

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='burlywood4', command = self.picker)
        self.pasirinkti_mygtukas.pack()

        self.mightysam.pack()
        self.myers.pack()
        self.cummings.pack()
        self.rodgers.pack()
        self.smokehouse.pack()
        self.uzdaryti_blues.pack()

    def picker(self):
        if self.dainu_boks.get() == "When The Hurt is Over":
            webbrowser.open(('https://music.youtube.com/watch?v=_w2LNOL4rmk'), new = 2)
        if self.dainu_boks.get() == "Don't Worry About Me":
            webbrowser.open(('https://music.youtube.com/watch?v=7fUawUJeSkg'), new = 2)
        if self.dainu_boks.get() == "I am so Lonely":
            webbrowser.open(('https://music.youtube.com/watch?v=2jXDxEBm1xA'), new = 2)
        if self.dainu_boks.get() == "I am Tired of These Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=qW8q0XxeNx4'), new = 2)
        if self.dainu_boks.get() == "Where You Been So Long":
            webbrowser.open(('https://music.youtube.com/watch?v=tBS-bL6y1As'), new = 2)
        if self.dainu_boks.get() == "If You Could See":
            webbrowser.open(('https://music.youtube.com/watch?v=newUETHByOc'), new = 2)
        if self.dainu_boks.get() == "Where Is the Love":
            webbrowser.open(('https://music.youtube.com/watch?v=zQcravZx7EI'), new = 2)
        if self.dainu_boks.get() == "A Soul That Has Been Abused":
            webbrowser.open(('https://music.youtube.com/watch?v=ATdKDp67Ylw'), new = 2)
        if self.dainu_boks.get() == "Other Side of the Tracks":
            webbrowser.open(('https://music.youtube.com/watch?v=WsKvmLWMN_o'), new = 2)
        if self.dainu_boks.get() == "If It Wasn't for Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=fD947SUdDN0'), new = 2)
        if self.dainu_boks.get() == "I Got the Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=PnXK2OP7V2A'), new = 2)
        if self.dainu_boks.get() == "Let You Slowly Bring Me Down":
            webbrowser.open(('https://music.youtube.com/watch?v=2ZR1Mkb_Grs'), new = 2)
        if self.dainu_boks.get() == "I am Tired of Your Jive":
            webbrowser.open(('https://music.youtube.com/watch?v=y-zmQC1La00'), new = 2)
        if self.dainu_boks.get() == "Burning Fire":
            webbrowser.open(('https://music.youtube.com/watch?v=QOqZlQ7nl1c'), new = 2)
        if self.dainu_boks.get() == "My Daily Wish":
            webbrowser.open(('https://music.youtube.com/watch?v=fbGS6gLUhw4'), new = 2)
        if self.dainu_boks.get() == "Coming from the Old School":
            webbrowser.open(('https://music.youtube.com/watch?v=dwpOTHAt8_U'), new = 2)
        if self.dainu_boks.get() == "Burning Fire":
            webbrowser.open(('https://music.youtube.com/watch?v=QOqZlQ7nl1c'), new = 2)
        if self.dainu_boks.get() == "Sad and Lonesome":
            webbrowser.open(('https://music.youtube.com/watch?v=GCfvKj7C7e0'), new = 2)
        if self.dainu_boks.get() == "Sleeping in the Ground":
            webbrowser.open(('https://music.youtube.com/watch?v=hIMkaETUpcY'), new = 2)
        if self.dainu_boks.get() == "Ninety Nine":
            webbrowser.open(('https://music.youtube.com/watch?v=HGEnvRIF5KU'), new = 2)
        if self.dainu_boks.get() == "Workin' Man Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=zt5SZFio4yI'), new = 2)
        if self.dainu_boks.get() == "Meet the Man":
            webbrowser.open(('https://music.youtube.com/watch?v=TGvkm8zY6T8'), new = 2)
        if self.dainu_boks.get() == "Need Somebody":
            webbrowser.open(('https://music.youtube.com/watch?v=MHtnzRmomOY'), new = 2)
        if self.dainu_boks.get() == "Lonely Bed":
            webbrowser.open(('https://music.youtube.com/watch?v=Sm8q1q9Oqn0'), new = 2)
        if self.dainu_boks.get() == "Little Bird":
            webbrowser.open(('https://music.youtube.com/watch?v=tcciSHKo5VM'), new = 2)
        if self.dainu_boks.get() == "Rumors":
            webbrowser.open(('https://music.youtube.com/watch?v=Fgw9-6ECAFI'), new = 2)
        if self.dainu_boks.get() == "Too Old To Grow Up":
            webbrowser.open(('https://music.youtube.com/watch?v=jMMF6z2HEaE'), new = 2)
        if self.dainu_boks.get() == "So Strong":
            webbrowser.open(('https://music.youtube.com/watch?v=TAJFYHTb4F8'), new = 2)
        if self.dainu_boks.get() == "Last Call":
            webbrowser.open(('https://music.youtube.com/watch?v=DMJgdb0LGDQ'), new = 2)
        if self.dainu_boks.get() == "Get Out of Here":
            webbrowser.open(('https://music.youtube.com/watch?v=5EHpHkqI394'), new = 2)
        if self.dainu_boks.get() == "Picasso Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=oUJbLSQZ3vA'), new = 2)
        if self.dainu_boks.get() == "Black Paris Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=RFBgE_61BPc'), new = 2)
        if self.dainu_boks.get() == "Blues is a Woman Woe is a Man":
            webbrowser.open(('https://music.youtube.com/watch?v=FFYSw9uNK2c'), new = 2)
        if self.dainu_boks.get() == "My Blues, My Woman and My Car":
            webbrowser.open(('https://music.youtube.com/watch?v=k4dh9bm3DH8'), new = 2)
        if self.dainu_boks.get() == "Black Coffee and Cigarettes":
            webbrowser.open(('https://music.youtube.com/watch?v=GRnQT6gmg10'), new = 2)
        if self.dainu_boks.get() == "The Boy Who Stole the Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=g0wu5vLX4Ug'), new = 2)
        if self.dainu_boks.get() == "Shame":
            webbrowser.open(('https://music.youtube.com/watch?v=UZ1vGjG7lu0'), new = 2)
        if self.dainu_boks.get() == "No Regrets":
            webbrowser.open(('https://music.youtube.com/watch?v=Y3x5RzSkovM'), new = 2)
        if self.dainu_boks.get() == "Tomorrow Isn't Promised":
            webbrowser.open(('https://music.youtube.com/watch?v=4x6o8kZe50w'), new = 2)
        if self.dainu_boks.get() == "Cadillac Ranch":
            webbrowser.open(('https://music.youtube.com/watch?v=PQ0Y3JwLw0g'), new = 2)      
        if self.dainu_boks.get() == "Cadillac in the Swamps":
            webbrowser.open(('https://music.youtube.com/watch?v=p8TXKF0s3so'), new = 2)
        if self.dainu_boks.get() == "Haints in my House":
            webbrowser.open(('https://music.youtube.com/watch?v=I_bHdWzTvlo'), new = 2)
        if self.dainu_boks.get() == "Go Down Moses":
            webbrowser.open(('https://music.youtube.com/watch?v=Yx_pDRBXDC4'), new = 2)
        if self.dainu_boks.get() == "Hoodoo You?":
            webbrowser.open(('https://music.youtube.com/watch?v=l0cNCHZTFGA'), new = 2)
        if self.dainu_boks.get() == "Creepin' Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=tQcDpXMKBHQ'), new = 2)
        if self.dainu_boks.get() == "Nice 'N' Round":
            webbrowser.open(('https://music.youtube.com/watch?v=prcsHtYoxpI'), new = 2)
        if self.dainu_boks.get() == "Crack Smokin' Blues":
            webbrowser.open(('https://music.youtube.com/watch?v=6AkgMobH8Q4'), new = 2)
        if self.dainu_boks.get() == "Bisquit Roller":
            webbrowser.open(('https://music.youtube.com/watch?v=0y3IIDAwJcc'), new = 2)
        if self.dainu_boks.get() == "Martin Luther \"The King\"":
            webbrowser.open(('https://music.youtube.com/watch?v=N_Ua5KE2iQY'), new = 2)
        if self.dainu_boks.get() == "American Dream":
            webbrowser.open(('https://music.youtube.com/watch?v=XtpB7NYfAyU'), new = 2)

    
    def pasirinkti_daina(self, value):
        if self.atlikeju_boks.get() == "Mighty Sam McClain":
            self.dainu_boks.config(value = self.mcclain_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Sam Myers":
            self.dainu_boks.config(value = self.myers_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Albert Cummings":
            self.dainu_boks.config(value = self.cummings_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Mighty Mo Rodgers":
            self.dainu_boks.config(value = self.rodgers_dainos)
            self.dainu_boks.current(0)
        if self.atlikeju_boks.get() == "Smokehouse":
            self.dainu_boks.config(value = self.smokehouse_dainos)
            self.dainu_boks.current(0)

    def open_mightysam(self):
        self.random_mightysam = ['https://music.youtube.com/watch?v=_w2LNOL4rmk',
                                'https://music.youtube.com/watch?v=7fUawUJeSkg',
                                'https://music.youtube.com/watch?v=2jXDxEBm1xA',
                                'https://music.youtube.com/watch?v=qW8q0XxeNx4',
                                'https://music.youtube.com/watch?v=tBS-bL6y1As',
                                'https://music.youtube.com/watch?v=newUETHByOc',
                                'https://music.youtube.com/watch?v=zQcravZx7EI',
                                'https://music.youtube.com/watch?v=ATdKDp67Ylw',
                                'https://music.youtube.com/watch?v=WsKvmLWMN_o',
                                'https://music.youtube.com/watch?v=fD947SUdDN0'
                            ]
        webbrowser.open(choice(self.random_mightysam), new = 2)

    def open_myers(self):
        self.random_sam_myers = ['https://music.youtube.com/watch?v=PnXK2OP7V2A',
                                'https://music.youtube.com/watch?v=2ZR1Mkb_Grs',
                                'https://music.youtube.com/watch?v=y-zmQC1La00',
                                'https://music.youtube.com/watch?v=QOqZlQ7nl1c',
                                'https://music.youtube.com/watch?v=fbGS6gLUhw4',
                                'https://music.youtube.com/watch?v=dwpOTHAt8_U',
                                'https://music.youtube.com/watch?v=QOqZlQ7nl1c',
                                'https://music.youtube.com/watch?v=GCfvKj7C7e0',
                                'https://music.youtube.com/watch?v=hIMkaETUpcY',
                                'https://music.youtube.com/watch?v=HGEnvRIF5KU'
                            ]
        webbrowser.open(choice(self.random_sam_myers), new = 2)

    def open_cummings(self):
        self.random_cummings = ['https://music.youtube.com/watch?v=zt5SZFio4yI',
                                'https://music.youtube.com/watch?v=TGvkm8zY6T8',
                                'https://music.youtube.com/watch?v=MHtnzRmomOY',
                                'https://music.youtube.com/watch?v=Sm8q1q9Oqn0',
                                'https://music.youtube.com/watch?v=tcciSHKo5VM',
                                'https://music.youtube.com/watch?v=Fgw9-6ECAFI',
                                'https://music.youtube.com/watch?v=jMMF6z2HEaE',
                                'https://music.youtube.com/watch?v=TAJFYHTb4F8',
                                'https://music.youtube.com/watch?v=DMJgdb0LGDQ',
                                'https://music.youtube.com/watch?v=5EHpHkqI394'
                            ]
        webbrowser.open(choice(self.random_cummings), new = 2)

    def open_rodgers(self):
        self.random_rodgers = ['https://music.youtube.com/watch?v=oUJbLSQZ3vA',
                                'https://music.youtube.com/watch?v=RFBgE_61BPc',
                                'https://music.youtube.com/watch?v=FFYSw9uNK2c',
                                'https://music.youtube.com/watch?v=k4dh9bm3DH8',
                                'https://music.youtube.com/watch?v=GRnQT6gmg10',
                                'https://music.youtube.com/watch?v=g0wu5vLX4Ug',
                                'https://music.youtube.com/watch?v=UZ1vGjG7lu0',
                                'https://music.youtube.com/watch?v=Y3x5RzSkovM',
                                'https://music.youtube.com/watch?v=4x6o8kZe50w',
                                'https://music.youtube.com/watch?v=PQ0Y3JwLw0g'
                            ]
        webbrowser.open(choice(self.random_rodgers), new = 2)
    
    def open_smokehouse(self):
        self.random_smokehouse = ['https://music.youtube.com/watch?v=p8TXKF0s3so',
                                'https://music.youtube.com/watch?v=I_bHdWzTvlo',
                                'https://music.youtube.com/watch?v=Yx_pDRBXDC4',
                                'https://music.youtube.com/watch?v=l0cNCHZTFGA',
                                'https://music.youtube.com/watch?v=tQcDpXMKBHQ',
                                'https://music.youtube.com/watch?v=prcsHtYoxpI',
                                'https://music.youtube.com/watch?v=6AkgMobH8Q4',
                                'https://music.youtube.com/watch?v=0y3IIDAwJcc',
                                'https://music.youtube.com/watch?v=N_Ua5KE2iQY',
                                'https://music.youtube.com/watch?v=XtpB7NYfAyU'
                            ]
        webbrowser.open(choice(self.random_smokehouse), new = 2)

    def uzdaryti(self):
        self.master.destroy()
    
langas = tk.Tk()
langas.title("Your daily dose of music")
langas.geometry("400x500")
langas.configure(bg = 'black')
programa = PagrindinisLangas(langas)
langas.mainloop()