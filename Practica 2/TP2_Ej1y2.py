texto= '''NumPy

NumPy is the fundamental package needed for scientific computing with Python.

    Website: https://www.numpy.org
    Documentation: https://numpy.org/doc
    Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
    Source code: https://github.com/numpy/numpy
    Contributing: https://www.numpy.org/devdocs/dev/index.html
    Bug reports: https://github.com/numpy/numpy/issues
    Report a security vulnerability: https://tidelift.com/docs/security

It provides:

    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires pytest. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()' '''

#Imprimo lass lineas que tengan http
lineas=texto.split("\n")
for i in lineas:
    if "http" in i.lower():
        print(i)

#La palabra que aparece la mayor cantidad de veces.
palabras=texto.lower().split()

from collections import Counter
contador = dict(Counter(palabras))
print(contador)
max=-1
for elem in contador:
    if contador[elem]>=max:
        max=contador[elem]
        palabramax=elem

print(f'{palabramax} aparece {max} veces.')
