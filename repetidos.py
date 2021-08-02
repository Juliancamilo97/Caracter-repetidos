def contar_caracteres_repetidos(cadena: str)->int:
    most_common_count = 0
    for letter in cadena:
        count = cadena.count(letter)
        if count > most_common_count:
            most_common_count = count
        if count==1:
            most_common_count=0
            
    return most_common_count

print(contar_caracteres_repetidos('geronim'))


def contar_caracteres_repetidos(cadena: str)->int:
    t=tuple(cadena)
    most_common_count=0
    lista=[]
    lista1=[]
    for i in range(len(t)):
            lista.append(t[i])
    for elemento in lista:
        if lista.count(elemento) > 1:
            lista1.append(elemento)
    if lista1==[]:
        most_common_count=0
    else:
        for letter in lista1:
            count = lista1.count(letter)
            if count > most_common_count:
                most_common_count = count
    return most_common_count