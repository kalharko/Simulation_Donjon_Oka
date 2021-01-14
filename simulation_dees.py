import random as rand
import numpy
from math import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


global NB_PLOT, STYLES, INTERESTING_PERCENT
NB_PLOT = 0
STYLES = []


#returns xdy exploding dices
def xdy_explo(x,y):
    out = 0
    for i in range(x):
        while True:
            roll = rand.randint(1,y)
            out += roll
            if roll != y:
                break
    return out

#shorter names for xdy_explo
def d4x():
    return xdy_explo(1,4)

def d6x():
    return xdy_explo(1,6)


#return a xdy roll
def xdy(x,y):
    out = 0
    for i in range(x):
        out += rand.randint(1,y)
    return out

#shorter names for xdy
def d6():
    return xdy(1,6)

#takes the raw simulation results and returns a list of tuples like so (value, occurence)
def sim_cleanup(sim):
    out = []
    maxi = max(sim)
    mini = min(sim)
    for value in range(mini-1, maxi+1):
        out.append((value, sim.count(value)))
    return out


#returns the mean from a cleaned up simulation result
def cleansim_mean(sim):
    total = 0
    div = 0
    for value in sim:
        total += value[0]*value[1]
        div += value[1]

    return total/div


#takes cleaned up simulation results and changes the occurence to pourcentages
def cleansim_percent(sim):
    global INTERESTING_PERCENT
    total = 0
    out = []
    for value in sim:
        total += value[1]

    #parcour la liste depuis la fin pour trouver la première valeur dont le % est >0.1
    shortsim = sim
    for i in range(1, len(sim)-1):
        if sim[-i][1]/total*100 >INTERESTING_PERCENT:
            shortsim = sim[:-i]
            break

    for value in shortsim:
        out.append((value[0], value[1] / total*100))

    return out


#takes cleaned up simulation results and changes the occurence following y=exp(x) curve
def cleansim_exp(sim):
    out = []
    for value in sim:
        if value[1] <= 0 :
            out.append((value[0], value[1]))
        else:
            out.append((value[0], math.log(value[1])))
    return out


#makes a matplotlib graph out of a cleaned up sim
def cleansim_graph(sim, name):
    global NB_PLOT, STYLES
    ptsx, ptsy = [], []

    for tupel in sim:
        ptsx.append(tupel[0])
        ptsy.append(tupel[1])


    #plt.axes(frameon=False)
    #plt.axhline(y=0, alpha=0.4)
    plt.title("moyenne : "+str(round(cleansim_mean(sim),2)) + "\n" + name)
    ax = plt.axes()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    plt.axhline(y=0, alpha=0.4)
    plt.axvline(x=0, alpha=0.4)
    plt.plot(ptsx, ptsy, STYLES[NB_PLOT])
    NB_PLOT += 1

    #plt.show()



def simulate_and_graph(formule):
    sim = simulate_roll(formule)
    cleansim_graph(cleansim_percent(sim), formule)


def simulate_roll(formule, iterations=500000):
    sim = [] #raw simulation results
    for i in range(iterations):
        roll = eval(formule)
        sim.append(roll)
    return sim_cleanup(sim)

"""---------------------"""
"""    Graph Styles   """
NB_PLOT = 0
STYLES = ["kx", "bx", "r+", "g+"]
INTERESTING_PERCENT = 0.1 #usualy 0.1

"""---------------------8.2-9.2-9.98"""
""" USER INTERFACE """



#plt.title("Noir: 2d6 explo, Bleu: max(1d6,1d6)")
# plt.show()














#eof
