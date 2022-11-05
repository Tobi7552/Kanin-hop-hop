import PySimpleGUI as sg
def gui():
    gui1 =[[sg.Text('Kanin hop hop')],
    [sg.Text('Antal spillere'),sg.Input(2,key = '-s-')],
    [sg.Text('Antal gentagelser'),sg.Input(10,key = '-n-')],
    [sg.Button('Lav graf')],
    [sg.Radio('Langsom','RADIO1', key = '-L-'),sg.Radio('Normal','RADIO1', key = '-N-'),sg.Radio('Hurtig','RADIO1', key = '-H-')],
    [sg.Graph(canvas_size=(600, 550),
                graph_bottom_left=(0, 0),
                graph_top_right=(600, 550),
                key='-graph-',
                background_color ='#242834')],
    
    ]
    return gui1

     
     