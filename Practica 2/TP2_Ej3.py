texto="""For instance, on the planet Earth, man had always assumed that he was 
more intelligent than dolphins because he had achieved so much, the wheel, 
New York, wars and so on, whilst all the dolphins had ever done was muck about 
in the water having a good time. But conversely, the dolphins had always believed 
that they were far more intelligent than man, for precisely the same reasons."""
letra=input('Inserte una letra: ')
if len(letra)==1 and letra.isalpha():
    for palabra in texto.lower().split():
        if palabra.strip().startswith(letra.lower()):
            print(palabra)
else:
    print('Usted no ha ingresado una letra.')