cadena=input('Ingresa la clave(debe tener menos de 10 caracteres y no contener los simbolos @ y !): ')
if len(cadena)>10:
    print('INgresaste mas de 10 caracteres.')
if '@' or '!' in cadena:
    print("Ingresaste un @ o un !.")
else:
    print('Ingreso correcto :)')
