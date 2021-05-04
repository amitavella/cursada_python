import PySimpleGUI as sg
import json
import csv

def analizar_paises():
    #Abro archivos, analizo los datos y los guardo en un archivo con formato json
    arch=open('flag.csv','r')
    csvreader=csv.reader(arch,delimiter=",")
    lista=[]
    dic={}
    #Guardo los paises de America donde se habla español 
    for linea in csvreader:
        if linea[1] in ["1","2"] and linea[5]=="2":
            dic["Pais"]=linea[0]
            dic["Area"]=linea[3]
            dic["Religion oficial"]=linea[6]
            lista.append(dic.copy())
    archjson=open('data_paises.txt','w')
    json.dump(lista,archjson)
    mostrar=json.dumps(lista,indent=4)
    archjson.close()
    arch.close()

    layout = [[sg.Text(mostrar)],
    [sg.Button('Salir', size=(50, 2))]]

    window = sg.Window('Analisis paises ',layout)
    
    while True:
         event, values = window.read()
         if event in (sg.WIN_CLOSED, 'Salir'):
             break
    window.close()

