import random
import pandas as pd
import PySimpleGUI as sg
import numpy as np
# import various funtions from matplotlib
import matplotlib 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from gui import *



fig_gui = None
layout = gui()
window = sg.Window('Kanin hop hop', layout = layout, element_justification='center', finalize = True)

#funktioner til at lave grafen med
def draw_figure(canvas, figure):
    """
    #Draws figure on canvas for GUI
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def delete_fig(fig):
    """
    #Deletes figure from plot
    """
    fig.get_tk_widget().forget()
    plt.close('all')


def check_winner(spillere):
    diller = [i for i, x in enumerate(spillere) if x == max(spillere)]
    return diller
            
def runde(players,vindere):
    for i in range(len(players)):
        vindere[players[i]] += 1
    return vindere   

def monte(n,vindere,l1): 
    for i in range(len(l1)):
        ni = vindere[i]
        l1[i].append(ni / n  *100)
    return l1
                 

def make_plot(l1,n):
    fig, ax = plt.subplots()
    for i in range(len(l1)):
        ax.plot(l1[i],label = f'Player{i+1}')
        
    ax.legend()    
    tf = int(n/5)
    if tf < 5:
        tf = 1
    ax.set_xticks(range(0,n+1,tf))
    return fig

    
def main(n,s):
    spillere = [0] * s
    vindere = [0] * s
    diller = normal(vindere,n,s)
    return diller
    
    #print(l1)
def normal(vindere,n,s):
    colors = ['red','green','blue','orange','yellow','rabbit']
    l1 = []
    for i in range(s):
        l1.append([])
    for j in range(1,n+1):
        spillere = [0] * s
        kanin = 20
        if N == 1:
            while kanin > 0:
                    for i in range(len(spillere)):
                        slag = random.choice(colors)
                        if slag == 'reda':
                            spillere[i]+=  1
                            colors[0] = 'red'
                        elif slag == colors[0]:
                            kanin -= 1
                            colors[0] = colors[0]+'a'
                        if slag == 'greena':
                            spillere[i] += 1
                            colors[1] = 'green'
                        elif slag == colors[1]:
                            kanin -= 1
                            colors[1] = colors[1]+'a'
                        if slag == 'bluea':
                            spillere[i] += 1
                            colors[2] = 'blue'
                        elif slag == colors[2]:
                            kanin -= 1
                            colors[2] = colors[2]+'a'
                        if slag == 'orangea':
                            spillere[i] += 1
                            colors[3] = 'orange'
                        elif slag == colors[3]:
                            kanin -= 1
                            colors[3] = colors[3]+'a'
                        if slag == 'yellowa':
                            spillere[i] += 1
                            colors[4] = 'yellow'
                        elif slag == colors[4]:
                            kanin -= 1
                            colors[4] = colors[4]+'a'
                        if slag == colors[5]:
                            spillere[i] += 1
                            kanin -= 1
                        if kanin < 1:
                            break
        if L == 1:
            while kanin > 0:
                    for i in range(len(spillere)):
                        slag = random.choice(colors)
                        if slag == 'reda':
                            spillere[i]+=  1
                            colors[0] = 'red'
                        elif slag == colors[0]:
                            kanin -= 1
                            colors[0] = colors[0]+'a'
                        if slag == 'greena':
                            spillere[i] += 1
                            colors[1] = 'green'
                        elif slag == colors[1]:
                            kanin -= 1
                            colors[1] = colors[1]+'a'
                        if slag == 'bluea':
                            spillere[i] += 1
                            colors[2] = 'blue'
                        elif slag == colors[2]:
                            kanin -= 1
                            colors[2] = colors[2]+'a'
                        if slag == 'orangea':
                            spillere[i] += 1
                            colors[3] = 'orange'
                        elif slag == colors[3]:
                            kanin -= 1
                            colors[3] = colors[3]+'a'
                        if slag == 'yellowa':
                            spillere[i] += 1
                            colors[4] = 'yellow'
                        elif slag == colors[4]:
                            kanin -= 1
                            colors[4] = colors[4]+'a'
                        if slag == colors[5]:
                            if spillere[i] == 0:
                                pass
                            else:
                                spillere[i] -= 1
                                kanin += 1
                        if kanin < 1:
                            break 
        if H == 1:
            while kanin > 0:
                    for i in range(len(spillere)):
                        print(i)
                        slag = random.choice(colors)
                        if slag == 'reda':
                            spillere[i]+=  1
                            colors[0] = 'red'
                        elif slag == colors[0]:
                            kanin -= 1
                            colors[0] = colors[0]+'a'
                        if slag == 'greena':
                            spillere[i] += 1
                            colors[1] = 'green'
                        elif slag == colors[1]:
                            kanin -= 1
                            colors[1] = colors[1]+'a'
                        if slag == 'bluea':
                            spillere[i] += 1
                            colors[2] = 'blue'
                        elif slag == colors[2]:
                            kanin -= 1
                            colors[2] = colors[2]+'a'
                        if slag == 'orangea':
                            spillere[i] += 1
                            colors[3] = 'orange'
                        elif slag == colors[3]:
                            kanin -= 1
                            colors[3] = colors[3]+'a'
                        if slag == 'yellowa':
                            spillere[i] += 1
                            colors[4] = 'yellow'
                        elif slag == colors[4]:
                            kanin -= 1
                            colors[4] = colors[4]+'a'
                        if slag == colors[5]:
                        
                            spillere[i] += 1
                            kanin -= 1
                            i = i
                            print(i)
                        if kanin < 1:
                            break  
        vindere = runde(check_winner(spillere),vindere)
        l1 = monte(j,vindere,l1)
    return l1 

           
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Lav graf':
        N = 0
        L = 0
        H = 0
        s = int(values['-s-'])
        if values['-N-'] == True:
            N = 1
            print(N)
            l1 = main(int(values['-n-']),s)
            if fig_gui != None:
                delete_fig(fig_gui)
            fig_gui = make_plot(l1,int(values['-n-']))
            fig_gui = draw_figure(window['-graph-'].TKCanvas, fig_gui)
        elif values['-L-'] == True:
            L = 1
            print(L)
            l1 = main(int(values['-n-']),s)
            if fig_gui != None:
                delete_fig(fig_gui)
            fig_gui = make_plot(l1,int(values['-n-']))
            fig_gui = draw_figure(window['-graph-'].TKCanvas, fig_gui)
        elif values['-H-'] == True:
            H = 1
            print(L)
            l1 = main(int(values['-n-']),s)
            if fig_gui != None:
                delete_fig(fig_gui)
            fig_gui = make_plot(l1,int(values['-n-']))
            fig_gui = draw_figure(window['-graph-'].TKCanvas, fig_gui)
    
window.close()