import csv
import json
import PySimpleGUI as sg
import paises

layout = [[sg.Text("Datos a analizar:")],
    [sg.Button('Analises de paises', size=(50, 2), key="datos1")],
    [sg.Button('Alojamientos de Airbnb en la ciudad de Buenos Aires', size=(50, 2), key="datos2")],
    [sg.Button('Salir', size=(20, 2))]]

window = sg.Window('Analisis  de data',layout)

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == 'Salir' or event == sg.WINDOW_CLOSED:
        break
    if(event == 'datos1'):
        window.hide()
        paises.analizar_paises()
        window.un_hide()
    if(event == 'datos2'):
        window.hide()
        #Falta implementar
        window.un_hide()

