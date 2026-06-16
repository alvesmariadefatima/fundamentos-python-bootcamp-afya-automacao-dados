# A função copy() é utilizada para criar uma cópia rasa (shallow copy) de uma lista.
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)