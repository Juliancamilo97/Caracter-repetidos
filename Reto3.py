
'''
def contar_caracteres_repetidos(cadena: str)->int:
    t=tuple(cadena)
    rep=0
    lista=[]
    lista1=[]
    for i in range(len(t)):
            lista.append(t[i])
    for elemento in lista:
        if lista.count(elemento) > 1:
            lista1.append(elemento)
    if lista1==[]:
        lista2=0
    else:
        lista2=lista1.count(lista1[0])
            
    return lista2


print(contar_caracteres_repetidos('contador'))
'''

def contar_caracteres_repetidos(cadena: str)->int:
    
    letras_dic = dict()  #Guarda repetición de letras
    contador = 0 #Caracteres que se repiten

    for letra in cadena: #Por cada letra
        if letra in letras_dic: #Si ya estaba en el dic() significa que se repite
            if letras_dic[letra] == 1: 
                contador += 1 #Se agrega al contador
            letras_dic[letra] += 1 #Continua el conteo
        else:
            letras_dic[letra] = 1 #Si la letra no esta en el diccionario, la agrega
    return contador



print(contar_caracteres_repetidos('presidente'))