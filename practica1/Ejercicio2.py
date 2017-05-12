def max_de_tres(a, b, c):
    if a>b :
        if a>c :
            return (a)
        else :
            return (c)
    elif b>c :
        return (b)
    else:
        return (c)

print ("El valor mayor es: ", max_de_tres(a=int(input("Primer numero: ")), b=int(input("Segundo numero: ")), c=int(input("Tercer numero: "))))