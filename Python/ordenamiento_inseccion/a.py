def ordenamiento_por_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i
        
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion = posicion - 1
        
        lista[posicion] = valor_actual
    
    return lista