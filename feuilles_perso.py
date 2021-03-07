#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random as rand
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from simulation_dees import *
from radar import *




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

    def Display_Graphs(self):
            #simulate rolls
        sim_att = []
        sim_att_av = []
        sim_def = []
        for x in range(60000):
            sim_att.append(self.Attaque())
            sim_att_av.append(self.Attaque_Avantage())
            sim_def.append(self.Defense())

            #makes clean data to plot
        sim_att = cleansim_percent(sim_cleanup(sim_att))
        sim_att_av = cleansim_percent(sim_cleanup(sim_att_av))
        sim_def = cleansim_percent(sim_cleanup(sim_def))

        plot_att = cleansim_good2plot(sim_att)
        plot_att_av = cleansim_good2plot(sim_att_av)
        plot_def = cleansim_good2plot(sim_def)
        # print(sim_att)
        # print(sim_att_av)

        fig, axs = plt.subplots(2, 2)
        fig.subplots_adjust(wspace=0.1, hspace=0.25, top=0.95, bottom=0.05, left=0.05, right=0.95)

        axs[0,0].plot(plot_att[0], plot_att[1], 'b+')
        axs[0,0].set_title('Attaque, moy='+str(round(cleansim_mean(sim_att),2)))
        axs[0,0].xaxis.set_major_locator(MultipleLocator(1))
        axs[0,0].axhline(y=0, alpha=0.4)
        axs[0,0].set(ylabel='Chances (%)')

        axs[0,1].plot(plot_att_av[0], plot_att_av[1], 'b+')
        axs[0,1].set_title('Attaque_Avantage, moy='+str(round(cleansim_mean(sim_att_av),2)))
        axs[0,1].xaxis.set_major_locator(MultipleLocator(1))
        axs[0,1].sharey(axs[0, 0])
        axs[0,1].axhline(y=0, alpha=0.4)

        axs[1,0].plot(plot_def[0], plot_def[1], 'tab:green')
        axs[1,0].set_title('Defense, moy='+str(round(cleansim_mean(sim_def),2)))
        axs[1,0].xaxis.set_major_locator(MultipleLocator(1))
        axs[1,0].set(xlabel='Valeur')


        #RADAR X)
        theta = radar_factory(7, frame='circle')
        axs[1,1] = plt.subplot(224, projection='radar')
        labels = ['Ingéniosité', 'Combat', 'Attaque(moy)',
                    'Attaque Avantage(moy)','Dégats', 'Protection',
                    'Défense (moy)']
        data = [self.Ingeniosite, self.Combat, cleansim_mean(sim_att),
                cleansim_mean(sim_att_av), self.Degats, self.Protection,
                cleansim_mean(sim_def)]

        axs[1,1].plot(theta, data, color='b')
        axs[1,1].fill(theta, data, facecolor='b', alpha=0.25)
        axs[1,1].set_varlabels(labels)


        plt.show()

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
        if self.Protection == 0:
            return 0
        else:
            return self.Protection + randint(1, self.Protection//2 + 1)

    def Set_Degats_from_Attaque(self, Att):
        self.Degats = ceil(0.8*Att - 0.6)

    def Graph_choix_Vie_Def(self, coup, PJ=[]):
        att_moy_PJ = 0
        for pj in PJ:
            att_moy_PJ += pj.Get_Mean("attaque")
        att_moy_PJ /= len(PJ)

        ptsx = []
        ptsy = []
        wholey = []
        for x in range(30):
            if coup*(att_moy_PJ - x) < 0:
                break
            ptsx.append(x)
            ptsy.append(coup*(att_moy_PJ - x))
            wholey.append(round(ptsy[-1]))

        #style
        plt.title("Choix Vie/Def pour PNJ")
        plt.xlabel('Defense')
        plt.ylabel('Vie')
        ax = plt.axes()
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        # plt.grid()

        #plot the line
        plt.plot(ptsx, ptsy, "k-")

        #plot whole values
        plt.plot(ptsx, wholey, "bs")
        plt.plot(range(0,max(ptsx)), range(0,max(ptsx)), "g--")

        plt.grid()
        plt.show()

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
