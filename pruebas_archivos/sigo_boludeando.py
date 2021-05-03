a1=open('NiIdea.txt','r')
print('-'*10+'Opcion 1'+'-'*10)
for linea in a1:
    print(linea)
print('-'*10+'Opcion 1'+'-'*10)
a1.seek(0,0)
for car in a1.read():
    print(car)
a1.close()