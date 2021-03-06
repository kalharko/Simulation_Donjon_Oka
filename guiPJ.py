import tkinter as tk
from feuilles_perso import *

class guiPJ():
    def __init__(self, P):

        self.P = P

        #tk
        self.root = tk.Tk()
        self.root.title('guiPJ')
        self.root.minsize(width=500, height=500)
        self.root.columnconfigure(0, weight = 1)
        self.root.columnconfigure(1, weight = 1)
        self.root.rowconfigure(0, weight = 2)
        self.root.rowconfigure(1, weight = 1)
        self.root.rowconfigure(2, weight = 1)


        self.label = tk.Label(self.root, bg="#aaa")
        self.label.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        self.frame_stats = tk.Frame(self.root, bg="#bbb")
        self.frame_stats.grid(row=0, column=1, sticky="nesw", padx=15, pady=15)
        self.frame_stats.columnconfigure(0, weight=1)
        self.frame_stats.columnconfigure(1, weight=1)
        self.frame_stats.rowconfigure(0, weight=1)
        self.frame_stats.rowconfigure(1, weight=1)

        self.stats = []
        self.stats.append(tk.Label(self.frame_stats, bg="#ccc"))
        self.stats.append(tk.Label(self.frame_stats, bg="#ccc"))
        self.stats.append(tk.Label(self.frame_stats, bg="#ccc"))
        self.stats.append(tk.Label(self.frame_stats, bg="#ccc"))
        self.stats[0].grid(row=0, column=0)
        self.stats[1].grid(row=1, column=0)
        self.stats[2].grid(row=0, column=1)
        self.stats[3].grid(row=1, column=1)
        self.update_stats_display()

        self.but_att = tk.Button(self.root, bg="#aaa", text="Attaque", command=self.button_att)
        self.but_att.grid(row=1, column=0, sticky="nesw", padx=10, pady=10)
        self.but_att_av = tk.Button(self.root, bg="#aaa", text="Attaque Avantage", command=self.button_att_av)
        self.but_att_av.grid(row=1, column=1, sticky="nesw", padx=10, pady=10)
        self.but_def = tk.Button(self.root, bg="#aaa", text="Defense", command=self.button_def)
        self.but_def.grid(row=2, column=0, sticky="nesw", padx=10, pady=10)
        self.but_att_nue = tk.Button(self.root, bg="#aaa", text="Attaque Main nue", command=self.button_att_nue)
        self.but_att_nue.grid(row=2, column=1, sticky="nesw", padx=10, pady=10)


        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.menubar.add_cascade(label="Perso", menu=self.filemenu)

        self.root.config(menu=self.menubar)

        self.root.mainloop()


    def update_stats_display(self):
        txt = ["Combat : ", "Degats arme : ", "Ingeniosite : ", "Protection : "]
        value = [self.P.Combat, self.P.Degats, self.P.Ingeniosite, self.P.Protection]
        for i in range(4):
            self.stats[i]["text"]= txt[i]+str(value[i])

    def button_att(self):
        self.label["text"] = str(self.P.Attaque())

    def button_att_av(self):
        self.label["text"] = str(self.P.Attaque_Avantage())

    def button_att_nue(self):
        self.label["text"] = str(self.P.Attaque_Main_Nue())

    def button_def(self):
        self.label["text"] = str(self.P.Defense())


gui = guiPJ(PJ(8,6,4,1,6))
