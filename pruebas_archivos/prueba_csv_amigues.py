import csv
arch=open('amigues.csv','r')
csvreader=csv.reader(arch,delimiter=",")
print("Nombre"+" "*30+"Ocupacion")
for linea in csvreader:
    if 'a' in linea[0]:
        print(f"{linea[0]:<35} {linea[3]:<35}")
print(type(linea))
print(csvreader)
arch.close()