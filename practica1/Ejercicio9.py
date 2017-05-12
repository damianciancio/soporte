def generar_n_caracteres(nro,letra):
    palabra=""
    for i in range(0, nro):
        palabra += letra
    return palabra

print(generar_n_caracteres(4, 'n'))
