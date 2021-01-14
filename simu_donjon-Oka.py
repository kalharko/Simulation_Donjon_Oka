import random as rand
import numpy
from math import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from simulation_dees import *



#simulate donjon Oka attaque roll
def graph_attaque_PJ(combat, degats):
    simulate_and_graph(f"ceil((d6x()+{combat})/6*{degats})")

def graph_defense_PJ(Ingeniosite):
    simulate_and_graph(f"ceil((d6x()+{Ingeniosite})/6*{Ingeniosite})")


def graph_attaque_PNJ(degats):
    simulate_and_graph(f"ceil(rand.randint(1,100)/100*{degats})")

def graph_defense_PNJ(defense):
    simulate_and_graph(f"ceil(rand.randint(1,100)/100*{defense})")


#simulate a roll minus the other
def graph_attaquePJ_vs_defensePNJ(combat, degats, defense):
    simulate_and_graph(f"ceil((d6x()+{combat})/6*{degats}) - ceil(rand.randint(1,100)/100*{defense})")


graph_attaquePJ_vs_defensePNJ(4,6,10)

plt.show()
#eof
