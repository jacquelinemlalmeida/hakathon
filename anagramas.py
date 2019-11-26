import re
import sys
from dicionarios import calcula_quantidade_letras

if len(sys.argv) <= 1:
    print('Você precisa passar uma palavra')
    sys.exit()

# a string de entrada BELA tem muitos anagramas
string = sys.argv[1]
dict_letras_1 = {}
dict_letras_2 = {}
anagramas = []
string=string.upper();

string = string.replace(" ","")

x = re.findall(r"[!#$%&'()*+,-./:;?@[\\\]_`{|}~0-9\*]", string)

if(len(x)>0):
    print("Não use caracteres especiais!")
    exit()

with open("palavras.txt") as arquivo:
    for palavra in arquivo:
        palavra = palavra.replace("\n","")
        dict_letras_1 = calcula_quantidade_letras(string)
        dict_letras_2 = calcula_quantidade_letras(palavra)
        if(dict_letras_1==dict_letras_2):
            anagramas.append(palavra)

print(anagramas)



