import json
arc=open('otro_archivo.txt','a')
listdict=[]
dict={}
nombre=input('Ingrese su nombre: ')
while nombre != 'fin':
    edad=int(input("Ingrese su edad: "))
    ocup=input('Ingrese su ocupacion: ')
    dict['nombre']=nombre
    dict['edad']=edad
    dict['ocupacion']=ocup
    listdict.append(dict.copy())
    nombre=input('Ingrese su nombre: ')
json.dump(listdict,arc)
arc.close()