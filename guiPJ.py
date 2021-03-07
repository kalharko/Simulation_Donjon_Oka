import tkinter as tk
import tkinter.font as tkFont
from feuilles_perso_light import *
from os import listdir

class guiPJ():
    def __init__(self, Ps):

        self.Ps = Ps
        self.P = self.Ps[0]

        #tk
        self.root = tk.Tk()
        self.root.title(self.P.Name)
        self.root.minsize(width=500, height=500)
        self.root.columnconfigure(0, weight = 1)
        self.root.columnconfigure(1, weight = 1)
        self.root.rowconfigure(0, weight = 2)
        self.root.rowconfigure(1, weight = 1)
        self.root.rowconfigure(2, weight = 1)
        self.root['bg'] = "#2f3136"

        self.Helvetica = tkFont.Font(family='Helvetica', weight='bold')
        self.BigHelvetica = tkFont.Font(family='Helvetica', weight='bold', size=54)
        # print(tkFont.families())

        #dice rollsdisplay
        self.label = tk.Label(self.root, bg="#36393f", font=self.BigHelvetica)
        self.label.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        #stats
        self.frame_stats = tk.Frame(self.root, bg="#36393f")
        self.frame_stats.grid(row=0, column=1, sticky="nesw", padx=15, pady=15)
        self.frame_stats.columnconfigure(0, weight=1)
        self.frame_stats.columnconfigure(1, weight=1)
        self.frame_stats.rowconfigure(0, weight=1)
        self.frame_stats.rowconfigure(1, weight=1)

        self.stats = []
        self.stats.append(tk.Label(self.frame_stats, bg="#393c43", fg="#9b9c9f", font=self.Helvetica))
        self.stats.append(tk.Label(self.frame_stats, bg="#393c43", fg="#9b9c9f", font=self.Helvetica))
        self.stats.append(tk.Label(self.frame_stats, bg="#393c43", fg="#9b9c9f", font=self.Helvetica))
        self.stats.append(tk.Label(self.frame_stats, bg="#393c43", fg="#9b9c9f", font=self.Helvetica))
        self.stats[0].grid(row=0, column=0)
        self.stats[1].grid(row=1, column=0)
        self.stats[2].grid(row=0, column=1)
        self.stats[3].grid(row=1, column=1)
        self.update_stats_display()

        #buttons
        self.but_att = tk.Button(self.root, bg="#36393f", text="Attaque", command=self.button_att, fg="#9b9c9f", font=self.Helvetica)
        self.but_att.grid(row=1, column=0, sticky="nesw", padx=10, pady=10)
        self.but_att_av = tk.Button(self.root, bg="#36393f", text="Attaque Avantage", command=self.button_att_av, fg="#9b9c9f", font=self.Helvetica)
        self.but_att_av.grid(row=1, column=1, sticky="nesw", padx=10, pady=10)
        self.but_def = tk.Button(self.root, bg="#36393f", text="Defense", command=self.button_def, fg="#9b9c9f", font=self.Helvetica)
        self.but_def.grid(row=2, column=0, sticky="nesw", padx=10, pady=10)
        self.but_att_nue = tk.Button(self.root, bg="#36393f", text="Attaque Main nue", command=self.button_att_nue, fg="#9b9c9f", font=self.Helvetica)
        self.but_att_nue.grid(row=2, column=1, sticky="nesw", padx=10, pady=10)

        #character selection meu
        self.persoId = tk.IntVar()
        self.menubar = tk.Menu(self.root, bg="#9b9c9f")
        self.persomenu = tk.Menu(self.menubar, tearoff=0)
        for i,p in enumerate(self.Ps):
            self.persomenu.add_radiobutton(label=p.Name, variable=self.persoId, value=i, command=self.swap_perso, accelerator=str(i+1))
        self.menubar.add_cascade(label="Perso", menu=self.persomenu)

        self.root.config(menu=self.menubar)

        #keyboard binds
        for i,p in enumerate(self.Ps):
            self.root.bind(str(i+1), self.quick_character_selection)

        self.root.mainloop()


    def update_stats_display(self):
        txt = ["Combat : ", "Degats arme : ", "Ingeniosite : ", "Protection : "]
        value = [self.P.Combat, self.P.Degats, self.P.Ingeniosite, self.P.Protection]
        for i in range(4):
            self.stats[i]["text"]= txt[i]+str(value[i])

    def button_att(self):
        self.label["font"] = self.BigHelvetica
        self.label["text"] = str(self.P.Attaque())

    def button_att_av(self):
        self.label["font"] = self.BigHelvetica
        self.label["text"] = str(self.P.Attaque_Avantage())

    def button_att_nue(self):
        self.label["font"] = self.BigHelvetica
        self.label["text"] = str(self.P.Attaque_Main_Nue())

    def button_def(self):
        self.label["font"] = self.BigHelvetica
        self.label["text"] = str(self.P.Defense())

    def swap_perso(self):
        self.P = self.Ps[self.persoId.get()]
        self.root.title(self.P.Name)
        self.update_stats_display()
        self.label["font"] = self.Helvetica
        self.label["text"] = self.P.Name

    def quick_character_selection(self, arg):
        key = arg.keysym
        self.persoId.set(str(int(key)-1))
        self.swap_perso()


characters = []
for path in listdir("saves"):
    name = path.split(".")[0]
    l = []
    with open("saves/"+path) as file:
        lines = file.readlines()
        for line in lines[1:]:
            l.append(int(line.split(":")[1].rstrip("\n")))

        if lines[0] == "PJ\n":
            characters.append(PJ(name,l[0],l[1],l[2],l[3],l[4]))
        elif lines[0] == "PNJ\n":
            characters.append(PNJ(name,l[0],l[1],l[2],l[3]))
        else:
            print("Error opening save file")

gui = guiPJ(characters)
