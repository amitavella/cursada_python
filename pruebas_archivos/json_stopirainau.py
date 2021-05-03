import json
f=open("otro_archivo.txt","r")
f.seek(0,0)
cont=json.load(f)
f.close()
dict={}
nombre=input('Ingrese su nombre: ')
while nombre != 'fin':
    edad=int(input("Ingrese su edad: "))
    ocup=input('Ingrese su ocupacion: ')
    dict['nombre']=nombre
    dict['edad']=edad
    dict['ocupacion']=ocup
    cont.append(dict.copy())
    nombre=input('Ingrese su nombre: ')

with open('otro_archivo.txt','w') as f:
    json.dump(cont,f)