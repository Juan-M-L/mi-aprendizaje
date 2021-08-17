#import re

"""
def is_palindrome(word):
    word = word.lower()
    return word[::-1]

result = is_palindrome("lever")

print(result)
"""

"""
def count_characters(string):
    count_dict={}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("Hello")
"""

"""
numeros = ["uno","dos","tres","cuatro"]

digitos = [1,2,3]

numeros_digitos = []

for i in zip(numeros,digitos):
    numeros_digitos.append(i)

print(numeros_digitos)
"""

#Función de búsqueda binaria.
"""
def busqueda_binaria (a_list,item):
    first_number=0
    last_number=len(a_list)-1
    found=False
    while first_number <= last_number and not found:
        mid=(first_number + last_number)//2
        if a_list[mid] == item:
            found=True
        else:
            if item < a_list[mid]:
                last_number = mid - 1
            else:
                first_number = mid + 1
    return found

numeros = [1,2,3,4,5,6,7]

print(busqueda_binaria(numeros,6))
"""

"""
def devolver_duplicados (a_list):
    dups=[]
    a_set = set()
    for item in a_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)
    return dups

lista=["hola","chau","hola","adios","hola","adios"]

print(devolver_duplicados(lista))
"""

#ejercicio
"""
list= [1,7,5,3,2]
new_list=[i*7 for i in list]
print (new_list)
"""

"""
def intersection(lista_boletos,boletos_ganadores):
    matches=[valor for valor in lista_boletos if valor in boletos_ganadores]
    return matches

lista_boletos= [1,31,51,11,21,29]
boletos_ganadores= [11,51]

print(intersection(lista_boletos,boletos_ganadores))
"""

"""
def intersection(lista_boletos,boletos_ganadores):
    lista_boletos = set(lista1)
    boletos_ganadores = set(lista2)
    return lista_boletos.intersection(boletos_ganadores)

lista1 = [1,31,51,11,21,29]
lista2 = [11,51]

print (intersection(lista1,lista2))
"""

"""
def find_unique_number(big_list,small_list):
    try:
        for item in big_list:
            if big_list[item] in small_list:
                continue
            if big_list[item] not in small_list:
                return big_list[item]
    except IndexError:
        return big_list[-1]

big_list = [1,31,51,12,21,11]
small_list = [1,31,51,11,21]

print (find_unique_number(big_list,small_list))
"""

"""
def find_unique_number(big_list,small_list):
    item = len(big_list)-1
    while item >= 0:
        if big_list[item] in small_list:
            item -= 1
            continue
        else:
            return big_list[item]
        

big_list = [1,31,51,29,11,21]
small_list = [1,31,51,11,21]

print(find_unique_number(big_list,small_list))
"""
