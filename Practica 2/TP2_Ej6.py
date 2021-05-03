frase="""Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple."""

#Copio la frase en una variable extra para poder eliminar caracteres no alfabeticos sin modificar el texto
frase1=frase
char_indeseables="!@#$%^&*()-_=+][}{\|;:'/?><.,"
for car in char_indeseables:
    frase1=frase1.replace(car,"")

#HAgo una lista con todas las palabras del texto incluido las repetidas
palabrasrepe=frase1.lower().split()

#En base a la lista anterior hago una nueva donde solo aparece una vez cada palabra
lista=[]
for elem in palabrasrepe:
    if elem not in lista:
        lista.append(elem)

print(lista)