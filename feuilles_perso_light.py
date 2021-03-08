#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from math import ceil

class P():
    def __init__(self):
        self.Name = "P_Name"
        self.Combat = 0
        self.Degats = 0
        self.Ingeniosite = 0
        self.Protection = 0
        self.Deplacement = 0
        self.Vie = 0


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
        crit = 0
        out = randint(1,6) + self.Combat
        while randint(1,16-self.Combat) == 1:
            crit += 1
            out += self.Degats
        return out,crit

    def Attaque_Avantage(self):
        crit = 0
        out = randint(1,6) + self.Combat
        while randint(1,16-self.Combat) == 1:
            crit += 1
            out += self.Degats
        while randint(1,16-self.Combat) == 1:
            crit += 1
            out += self.Degats
        return (out,crit)

    def Attaque_Main_Nue(self):
        return randint(1,6) + self.Combat//2

    def Defense(self):
        return self.Protection + randint(1, self.Ingeniosite)






class PNJ(P):
    def __init__(self, Name, Degats, Protection, Deplacement, Vie):
        super().__init__()
        self.Name = Name
        self.Degats = Degats
        self.Protection = Protection
        self.Deplacement = Deplacement
        self.Vie = Vie


    def Attaque(self):
        return self.Degats + randint(1,ceil(self.Degats/2)),0

    def Attaque_Avantage(self):
        return self.Degats + randint(1,ceil(self.Degats/2)) + randint(1,ceil(self.Degats/2)),0

    def Attaque_Main_Nue(self):
        if randint(1,ceil(self.Degats/2)) < 0:
            return 0
        else:
            return self.Degats - randint(1,ceil(self.Degats/2))

    def Defense(self):
        if self.Protection == 0:
            return 0
        else:
            return self.Protection + randint(1, self.Protection//2 + 1)
