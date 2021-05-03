fraseorig=input('Ingrese una frase o texto: ')
palabra=input('Ingrese palabra a buscar en el texto: ')

#Copio la frase original en otra variable para poder deshacerme de los caracteres no alfabeticos sin modificar la original.
frase=fraseorig
char_indeseables="!@#$%^&*()-_=+][}{\|;:'/?><.,"
for car in char_indeseables:
    frase=frase.replace(car,"")
cont=0
for  elem in frase.lower().split():   
    if elem.lower()==palabra.lower():
        cont += 1
print(cont)
print(frase)
print(fraseorig)