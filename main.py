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

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.vidinis.title("\U0001F918 Rock")
        self.vidinis.configure(bg = "red")
        self.vidinis.geometry("430x400")
        self.app = VidinisRock(self.vidinis)

    def new_window2(self):
        self.vidinis2 = tk.Toplevel(self.master)
        self.vidinis2.title("\u262E Reggae")
        self.vidinis2.configure(bg = "green")
        self.vidinis2.geometry("430x400")
        self.app = VidinisReggae(self.vidinis2)

    def new_window3(self):
        self.vidinis3 = tk.Toplevel(self.master)
        self.vidinis3.title("\U0001F3B8 Heavy Metal")
        self.vidinis3.configure(bg = "grey")
        self.vidinis3.geometry("430x400")
        self.app = VidinisHeavyMetal(self.vidinis3)
    
    def new_window4(self):
        self.vidinis4 = tk.Toplevel(self.master)
        self.vidinis4.title("\U0001F577 Punk")
        self.vidinis4.configure(bg = "MediumPurple4")
        self.vidinis4.geometry("430x400")
        self.app = VidinisPunk(self.vidinis4)

    def new_window5(self):
        self.vidinis5 = tk.Toplevel(self.master)
        self.vidinis5.title("\U0001F480 Black Metal")
        self.vidinis5.configure(bg = "midnight blue")
        self.vidinis5.geometry("300x200")
        self.app = VidinisBlackMetal(self.vidinis5)

    def new_window6(self):
        self.vidinis6 = tk.Toplevel(self.master)
        self.vidinis6.title("\U0001F576 Rap")
        self.vidinis6.configure(bg = "IndianRed4")
        self.vidinis6.geometry("300x200")
        self.app = VidinisRap(self.vidinis6)

    def new_window7(self):
        self.vidinis7 = tk.Toplevel(self.master)
        self.vidinis7.title("\U0001F46F Pop")
        self.vidinis7.configure(bg = "hot pink")
        self.vidinis7.geometry("300x200")
        self.app = VidinisPop(self.vidinis7)

    def new_window8(self):
        self.vidinis8 = tk.Toplevel(self.master)
        self.vidinis8.title("\U0001F4BF Disco")
        self.vidinis8.configure(bg = "cyan")
        self.vidinis8.geometry("300x200")
        self.app = VidinisDisco(self.vidinis8)

    def new_window9(self):
        self.vidinis9 = tk.Toplevel(self.master)
        self.vidinis9.title("\U0001F3B7 Jazz")
        self.vidinis9.configure(bg = "DarkGoldenrod1")
        self.vidinis9.geometry("300x200")
        self.app = VidinisJazz(self.vidinis9)

    def new_window10(self):
        self.vidinis10 = tk.Toplevel(self.master)
        self.vidinis10.title("\U0001FA95 Blues")
        self.vidinis10.configure(bg = "burlywood4")
        self.vidinis10.geometry("300x200")
        self.app = VidinisBlues(self.vidinis10)

class VidinisRock:
    def __init__(self, master):
        self.master = master
        self.queen = tk.Button(self.master, text = "Queen", width = 15, command = self.open_qeen, highlightbackground='red')
        self.acdc = tk.Button(self.master, text = "AC/DC", width = 15, command = self.open_acdc, highlightbackground='red')
        self.doors = tk.Button(self.master, text = "The Doors", width = 15, command = self.open_doors, highlightbackground='red')
        self.ledzep = tk.Button(self.master, text = "Led Zeppelin", width = 15, command = self.open_ledzep, highlightbackground='red')
        self.deep_purple = tk.Button(self.master, text = "Deep Purple", width = 15, command = self.open_deep_purple, highlightbackground='red')
        self.uzdarytirock = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti, highlightbackground='red') 
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
        self.atlikeju_boks.pack()
        # bindinam boksą
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)

        # kuriam kitą boksą
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.pack()

        # pasirinkimo mygtukas
        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='red', command = self.picker)
        self.pasirinkti_mygtukas.pack()
       
        self.queen.pack()
        self.acdc.pack()
        self.doors.pack()
        self.ledzep.pack()
        self.deep_purple.pack()
        self.uzdarytirock.pack()

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
        self.uzdarytireggae = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti, highlightbackground='green')
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
        self.atlikeju_boks.pack()
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkta_daina)

        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.pack()

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='green', command = self.picker)
        self.pasirinkti_mygtukas.pack()


        self.bobm.pack()
        self.peter.pack()
        self.mouse.pack()
        self.damianm.pack()
        self.albarosie.pack()
        self.uzdarytireggae.pack()


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
        self.uzdaryti_metal = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti, highlightbackground='grey')
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
        self.atlikeju_boks.pack()
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.pack()

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='grey', command = self.picker)
        self.pasirinkti_mygtukas.pack()


        self.ironm.pack()
        self.blacksab.pack()
        self.judasp.pack()
        self.dio.pack()
        self.saxon.pack()
        self.uzdaryti_metal.pack()
        
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
        self.uzdaryti_punk = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti, highlightbackground="MediumPurple4")
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
                                " Shining",
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
        self.atlikeju_boks.pack()
        self.atlikeju_boks.bind("<<ComboboxSelected>>", self.pasirinkti_daina)
        self.dainu_boks = ttk.Combobox(self.master, value = [' '])
        self.dainu_boks.current(0)
        self.dainu_boks.pack()

        self.pasirinkti_mygtukas = tk.Button(self.master, text = 'Pasirinkti', highlightbackground='MediumPurple4', command = self.picker)
        self.pasirinkti_mygtukas.pack()
        self.ramones.pack()
        self.sexpistols.pack()
        self.offspring.pack()
        self.misfits.pack()
        self.clash.pack()
        self.uzdaryti_punk.pack()

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
        self.uzdaryti_bmetal = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground='midnight blue')
        self.mayhem.pack()
        self.marduk.pack()
        self.luctus.pack()
        self.watain.pack()
        self.behemoth.pack()
        self.uzdaryti_bmetal.pack()


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
        self.uzdaryti_rap = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground='IndianRed4')
        self.eminem.pack()
        self.snoop.pack()
        self.pac.pack()
        self.nwa.pack()
        self.lamar.pack()
        self.uzdaryti_rap.pack()

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
        self.uzdaryti_pop = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground='hot pink')
        self.ladygaga.pack()
        self.beyonce.pack()
        self.britneysp.pack()
        self.chaguilera.pack()
        self.justint.pack()
        self.uzdaryti_pop.pack()

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
        self.dsummer = tk.Button(self.master, text = "Donna Summer.", width = 15, command = self.open_dsummer, highlightbackground='cyan')
        self.uzdaryti_disco = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground='cyan')
        self.abba.pack()
        self.beegees.pack()
        self.sandra.pack()
        self.boneym.pack()
        self.dsummer.pack()
        self.uzdaryti_disco.pack()

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
        self.uzdaryti_jazz = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti, highlightbackground = "DarkGoldenrod1")
        self.candyd.pack()
        self.amstrong.pack()
        self.fitzgerald.pack()
        self.countb.pack()
        self.ninasimone.pack()
        self.uzdaryti_jazz.pack()

    
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
                                    'https://music.youtube.com/watch?v=KpDth46l_Vg'
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
        self.mightysam.pack()
        self.myers.pack()
        self.cummings.pack()
        self.rodgers.pack()
        self.smokehouse.pack()
        self.uzdaryti_blues.pack()

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