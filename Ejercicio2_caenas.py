#Ejercicio cadenas de texto

from unicodedata import name


name = input("Ingresa tu nombre ")
#cadenas indice

#print(archive[-4:])

#Validar extensiones
#if archive[-4:] != '.txt' or  archive[-4:] != '.json':
    #print("extension invalida")

#buscar indice de un caracter
#print(archive.find("s"))
#print(archive.index("s"))

#remplazar caracteres
#print(archive.replace('ñ','n'))

print("Hola {nombre_del_usuario}".format(nombre_del_usuario = name))