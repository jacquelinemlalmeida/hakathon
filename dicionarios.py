import string as str

def calcula_quantidade_letras(string):
    a = list(str.ascii_uppercase)

    dicionario_letras = {}

    for letras in a:
        dicionario_letras[letras]=0

    for letras in string:
        dicionario_letras[letras] = dicionario_letras[letras]+1

    return dicionario_letras




