def mas_larga(list1):
    longest = ""
    for i in list1:
        if len(i) > len(longest):
            longest = i
    return longest


list1 = ["Arbol", "Ayer", "Caminante", "Pez"]
print(mas_larga(list1))
