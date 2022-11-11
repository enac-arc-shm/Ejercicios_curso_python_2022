#Ejercicio cadenas de texto

from unicodedata import name

archivo = input("Ingresa el nombre de un archivo", end="")
#cadenas indice

print(archivo[-4:])

#Validar extensiones
if archivo[-4:] != '.txt':
    if archivo[-4:] != '.json':
        print("extension invalida")
print("cualquier cosa")
#buscar indice de un caracter
#print(archive.find("s"))
#print(archive.index("s"))

#remplazar caracteres
#print(archive.replace('ñ','n'))

print("Hola {nombre_del_usuario}".format(nombre_del_usuario = name))