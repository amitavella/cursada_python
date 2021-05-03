a1=open('NiIdea.txt','a+')
texto=input('Ingrese texto a guardar: ')
while texto.lower() != 'fin':
    a1.write(f'\n{texto}')
    texto=input('Ingrese texto a guardar(fin para terminar): ')
a1.seek(0,0)
for x in a1.read():
    print(x)
print(a1.tell())
a1.close()