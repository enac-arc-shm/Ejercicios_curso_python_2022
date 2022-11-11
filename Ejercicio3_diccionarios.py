

numeros = [2,4,6,8,10,12]

diccionario = {"Nombre": "Juan",
"Edad":18, "Escuela":"UTTT",
"peso":50.9}

if __name__ == "__main__":
    print(numeros)
    #Agregar elemento
    numeros.append(14)
    #Agregar mas de un elemento
    numeros += [3,4,2]
    print(numeros)
    #eliminar elemento por index
    #item_eliminado = numeros.pop()
    #item_eliminado = numeros.pop(-1)
    #eliminar elemento por valor
    print(numeros.count(100))
    
    if 2 in numeros:
        item_eliminado = numeros.remove(2)
        if 2 in numeros:
            item_eliminado = numeros.remove(2)
            
    print(numeros)