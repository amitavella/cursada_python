import json
arch=open('otro_archivo.txt','r')
datos=json.load(arch)
datos2=json.dumps(datos)
datos3=json.loads(datos2)
print(type(datos))
print(type(datos2))
print(type(datos3))
arch.close()
