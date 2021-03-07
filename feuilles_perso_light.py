#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as rand


class P():
    def __init__(self):
        self.Name = "P_Name"
        self.Combat = 0
        self.Degats = 0
        self.Ingeniosite = 0
        self.Protection = 0
        self.Deplacement = 0
        self.Vie = 0

    def Attaque(self):
        return 0
    def Attaque_Avantage(self):
        return 0
    def Attaque_Main_Nue(self):
        return 0
    def Defense(self):
        return 0;

    def Get_Mean(self, attribute):
        attributes = ["attaque", "attaque avantage", "defense"]
        formules = ["self.Attaque()", "self.Attaque_Avantage()", "self.Defense()"]
        if attribute in attributes:
            for i in range(len(attributes)):
                if attribute == attributes[i]:
                    formule = formules[i]
        else:
            return 0
        total = 0
        for i in range(60000):
            total += eval(formule)
        return round(total/60000, 2)


    def Print_Carac(self):
        print("Combat", self.Combat)
        print("Degats", self.Degats)
        print("Ingeniosite", self.Ingeniosite)
        print("Protection", self.Protection)
        print("Deplacement", self.Deplacement)
        print("Vie", self.Vie)


class PJ(P):
    def __init__(self, Name, Combat, Degats_arme, Ingeniosite, Protection_armure, Vie):
        super().__init__()
        self.Name = Name
        self.Combat = Combat
        self.Degats = Degats_arme
        self.Ingeniosite = Ingeniosite
        self.Protection = Protection_armure
        self.Vie = Vie

        self.Deplacement = 2*Ingeniosite


    def Attaque(self):
        out = rand.randint(1,6) + self.Combat
        while rand.randint(1,10) == 10:
            out += self.Degats
        return out

    def Attaque_Avantage(self):
        out = rand.randint(1,6) + self.Combat
        while rand.randint(1,10) == 10:
            out += self.Degats
        while rand.randint(1,10) == 10:
            out += self.Degats
        return out

    def Attaque_Main_Nue(self):
        return rand.randint(1,6) + self.Combat//2

    def Defense(self):
        return self.Protection + rand.randint(1, self.Ingeniosite)






class PNJ(P):
    def __init__(self, Name, Degats, Protection, Deplacement, Vie):
        super().__init__()
        self.Name = Name
        self.Degats = Degats
        self.Protection = Protection
        self.Deplacement = Deplacement
        self.Vie = Vie


    def Attaque(self):
        return self.Degats + rand.randint(1,ceil(self.Degats/2))

    def Attaque_Avantage(self):
        return self.Degats + rand.randint(1,ceil(self.Degats/2)) + rand.randint(1,ceil(self.Degats/2))

    def Attaque_Main_Nue(self):
        if rand.randint(1,ceil(self.Degats/2)) < 0:
            return 0
        else:
            return self.Degats - rand.randint(1,ceil(self.Degats/2))

    def Defense(self):
        return self.Protection + rand.randint(1, self.Protection//2 + 1)

    def Set_Degats_from_Attaque(self, Att):
        self.Degats = ceil(0.8*Att - 0.6)


    def Chose_Vie(self, coup, PJ=[]):
        att_moy_PJ = 0
        for pj in PJ:
            att_moy_PJ += pj.Get_Mean("attaque")
        att_moy_PJ /= len(PJ)
        print(f'att_moy_PJ = {att_moy_PJ}')
        self.Vie = ceil(att_moy_PJ * coup)

    def Graph_Attaque(self, coup, PJ=[]):
        def_moy_PJ = 0
        for pj in PJ:
            def_moy_PJ += pj.Get_Mean("defense")
        def_moy_PJ /= len(PJ)

        print(PJ.Vie/coup + def_moy_PJ)

    def Chose_Degats(self, coup, PJ=[]):
        def_moy_PJ = 0
        for pj in PJ:
            def_moy_PJ += pj.Get_Mean("defense")
        def_moy_PJ /= len(PJ)

        vie_moy_PJ = 0
        for pj in PJ:
            vie_moy_PJ += pj.Vie
        vie_moy_PJ /= len(PJ)
        print(f'def_moy_PJ = {def_moy_PJ},  vie_moy_PJ = {vie_moy_PJ}')
        Att = vie_moy_PJ/coup + def_moy_PJ
        self.Set_Degats_from_Attaque(Att)












mitri = PJ("Mitri", 8,6,4,1,6)
cothazan = PJ("Cothazan", 5,5,5,5,5)
wushang = PJ("Wushang", 1,1,3,10,10)

# wushang.Display_Graphs()

party = [mitri, cothazan, wushang]

araignee = PNJ("Araignee", 6,0,7,9)
robo = PNJ("robo", 7,0,4,26)
boss = PNJ("Boss", 9,4,3,52)

# araignee.Graph_choix_Vie_Def(1, party)
# boss.Chose_Degats(2, party)
# boss.Chose_Vie(6,party)

# robo.Display_Graphs()
# boss.Print_Carac()
#eof
