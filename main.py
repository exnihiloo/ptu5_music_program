from tkinter import *
import tkinter as tk
import webbrowser
from random import choice

class PagrindinisLangas:
    def __init__(self, master):
        self.master = master
        self.rock_langas = tk.Button(self.master, text = "\U0001F918 Rock", width = 15, command = self.new_window)
        self.reggae_langas = tk.Button(self.master, text = "\u262E Reggae", width = 15, command = self.new_window2)
        self.hmetal_langas = tk.Button(self.master, text = "\U0001F3B8 Heavy Metal", width = 15, command = self.new_window3)
        self.punk_langas = tk.Button(self.master, text = "\U0001F577 Punk", width = 15, command = self.new_window4)
        self.black_metal_langas = tk.Button(self.master, text = "\U0001F480 Black Metal", width = 15, command = self.new_window5)
        self.rap_langas = tk.Button(self.master, text = "\U0001F576 Rap", width = 15, command = self.new_window6)
        self.pop_langas = tk.Button(self.master, text = "\U0001F46F Pop", width = 15, command = self.new_window7)
        self.disco_langas = tk.Button(self.master, text = "\U0001F4BF Disco", width = 15, command = self.new_window8)
        self.rock_langas.pack()
        self.reggae_langas.pack()
        self.hmetal_langas.pack()
        self.punk_langas.pack()
        self.black_metal_langas.pack()
        self.rap_langas.pack()
        self.pop_langas.pack()
        self.disco_langas.pack()

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.vidinis.title("\U0001F918 Rock")
        self.app = VidinisRock(self.vidinis)

    def new_window2(self):
        self.vidinis2 = tk.Toplevel(self.master)
        self.vidinis2.title("\u262E Reggae")
        self.app = VidinisReggae(self.vidinis2)

    def new_window3(self):
        self.vidinis3 = tk.Toplevel(self.master)
        self.vidinis3.title("\U0001F3B8 Heavy Metal")
        self.app = VidinisHeavyMetal(self.vidinis3)
    
    def new_window4(self):
        self.vidinis4 = tk.Toplevel(self.master)
        self.vidinis4.title("\U0001F577 Punk")
        self.app = VidinisPunk(self.vidinis4)

    def new_window5(self):
        self.vidinis5 = tk.Toplevel(self.master)
        self.vidinis5.title("\U0001F480 Black Metal")
        self.app = VidinisBlackMetal(self.vidinis5)

    def new_window6(self):
        self.vidinis6 = tk.Toplevel(self.master)
        self.vidinis6.title("\U0001F576 Rap")
        self.app = VidinisRap(self.vidinis6)

    def new_window7(self):
        self.vidinis7 = tk.Toplevel(self.master)
        self.vidinis7.title("\U0001F46F Pop")
        self.app = VidinisPop(self.vidinis7)

    def new_window8(self):
        self.vidinis8 = tk.Toplevel(self.master)
        self.vidinis8.title("\U0001F4BF Disco")
        self.app = VidinisDisco(self.vidinis8)

class VidinisRock:
    def __init__(self, master):
        self.master = master
        self.queen = tk.Button(self.master, text = "Queen", width = 15, command = self.open_qeen)
        self.acdc = tk.Button(self.master, text = "AC/DC", width = 15, command = self.open_acdc)
        self.doors = tk.Button(self.master, text = "The Doors", width = 15, command = self.open_doors)
        self.ledzep = tk.Button(self.master, text = "Led Zeppelin", width = 15, command = self.open_ledzep)
        self.deep_purple = tk.Button(self.master, text = "Deep Purple", width = 15, command = self.open_deep_purple)
        self.uzdarytirock = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti) 
        self.queen.pack()
        self.acdc.pack()
        self.doors.pack()
        self.ledzep.pack()
        self.deep_purple.pack()
        self.uzdarytirock.pack()

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
        self.bobm = tk.Button(self.master, text = "Bob Marley & The Wailers", width = 15, command = self.open_bobm)
        self.peter = tk.Button(self.master, text = "Peter Tosh", width = 15, command = self.open_peter_tosh)
        self.mouse = tk.Button(self.master, text = "Eek-A-Mouse", width = 15, command = self.open_eekmouse)
        self.damianm = tk.Button(self.master, text = "Damian Marley", width = 15, command = self.open_damian_marley)
        self.albarosie = tk.Button(self.master, text = "Alborosie", width = 15, command = self.open_albarosie)
        self.uzdarytireggae = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti) 
        self.bobm.pack()
        self.peter.pack()
        self.mouse.pack()
        self.damianm.pack()
        self.albarosie.pack()
        self.uzdarytireggae.pack()

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
        self.ironm = tk.Button(self.master, text = "Iron Maiden", width = 15, command = self.open_ironm)
        self.blacksab = tk.Button(self.master, text = "Black Sabbath", width = 15, command = self.open_black_sab)
        self.judasp = tk.Button(self.master, text = "Judas Priest", width = 15, command = self.open_judasp)
        self.dio = tk.Button(self.master, text = "Dio", width = 15, command = self.open_dio)
        self.saxon = tk.Button(self.master, text = "Saxon", width = 15, command = self.open_saxon)
        self.uzdaryti_metal = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti)
        self.ironm.pack()
        self.blacksab.pack()
        self.judasp.pack()
        self.dio.pack()
        self.saxon.pack()
        self.uzdaryti_metal.pack()
        

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
        self.ramones = tk.Button(self.master, text = "Ramones", width = 15, command = self.open_ramones)
        self.sexpistols = tk.Button(self.master, text = "Sex Pistols", width = 15, command = self.open_sex_pistols)
        self.offspring = tk.Button(self.master, text = "The Offspring", width = 15, command = self.open_offspinrg)
        self.misfits = tk.Button(self.master, text = "Misfits", width = 15, command = self.open_misfits)
        self.clash = tk.Button(self.master, text = "The Clash", width = 15, command = self.open_clash)
        self.uzdaryti_punk = tk.Button(self.master, text = "\u2573 Uždaryti", command = self.uzdaryti)
        self.ramones.pack()
        self.sexpistols.pack()
        self.offspring.pack()
        self.misfits.pack()
        self.clash.pack()
        self.uzdaryti_punk.pack()

    
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
        self.mayhem = tk.Button(self.master, text = "Mayhem", width = 15, command = self.open_mayhem)
        self.marduk = tk.Button(self.master, text = "Marduk", width = 15, command = self.open_marduk)
        self.luctus = tk.Button(self.master, text = "Luctus", width = 15, command = self.open_luctus)
        self.watain = tk.Button(self.master, text = "Watain", width = 15, command = self.open_watain)
        self.behemoth = tk.Button(self.master, text = "Behemoth", width = 15, command = self.open_behemoth)
        self.uzdaryti_bmetal = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti)
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
        self.eminem = tk.Button(self.master, text = "Eminem", width = 15, command = self.open_eminem)
        self.snoop = tk.Button(self.master, text = "Snoop Dog", width = 15, command = self.open_snoop_dog)
        self.pac = tk.Button(self.master, text = "2Pac", width = 15, command = self.open_2pac)
        self.nwa = tk.Button(self.master, text = "N.W.A.", width = 15, command = self.open_nwa)
        self.lamar = tk.Button(self.master, text = "Kendrick Lamar", width = 15, command = self.open_kendric)
        self.uzdaryti_rap = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti)
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
        self.ladygaga = tk.Button(self.master, text = "Lady Gaga", width = 15, command = self.open_ladygaga)
        self.beyonce = tk.Button(self.master, text = "Beyoncé", width = 15, command = self.open_beyonce)
        self.britneysp = tk.Button(self.master, text = "Britney Spears", width = 15, command = self.open_britney)
        self.chaguilera = tk.Button(self.master, text = "Christina Aguilera", width = 15, command = self.open_christina)
        self.justint = tk.Button(self.master, text = "Justin Timberlake", width = 15, command = self.open_justint)
        self.uzdaryti_pop = tk.Button(self.master, text = "\u2573 Uždaryti", width = 15, command = self.uzdaryti)
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
        self.abba = tk.Button(self.master, text = "Abba", width = 15, command = self.open_abba)
        self.beegees = tk.Button(self.master, text = "Bee Gees", width = 15, command = self.open_beegees)
        self.sandra = tk.Button(self.master, text = "Sandra", width = 15, command = self.open_sandra)
        self.boneym = tk.Button(self.master, text = "Boney M.", width = 15, command = self.open_boneym)
        self.abba.pack()
        self.beegees.pack()
        self.sandra.pack()
        self.boneym.pack()

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

    
langas = tk.Tk()
langas.title("Shuffle Music")
programa = PagrindinisLangas(langas)
langas.mainloop()