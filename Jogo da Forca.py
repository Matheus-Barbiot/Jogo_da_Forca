import random
from unidecode import unidecode

def Llist(list):

    for L in list:
        print(L, end='')
    print('')
def lin(l='=', n=30):
    print(l * n)
def contlist(list, c):
    cont = 0
    for l in list:
        if l == c:
            cont += 1
    return cont
def contl(list):
    cont = 0
    for l in list:
        cont += 1
    return cont


#   INICIO, VARIAVEIS:
with open('Palavras.txt', 'r') as A:
    PALAVRAS_LIST = A.readlines()
    PALAVRAS_LIST = [L.rstrip('\n') for L in PALAVRAS_LIST]

PALAVRA_ = random.choice(PALAVRAS_LIST).lower()
A.close()

CHANCES_ = 6
ACERTOS_ = int(len(PALAVRA_))

BACKS_n = []
PALAVRA_n = []

lin
#   CRIANDO AS LISTAS:
for L_ in PALAVRA_:
    if L_ != ' ':
        BACKS_n.append('_')
    else:
        BACKS_n.append(' ')
        ACERTOS_ -= 1
for L_ in PALAVRA_:
    PALAVRA_n.append(L_)
Llist(BACKS_n)


#   CONDICIONANDO:
while ACERTOS_ != 0:
    CHUTE_ = str(input('Chute uma letra: ')).lower()[0]
    Z_ = contlist(PALAVRA_n, CHUTE_)
    lin()
#   COLOCANDO AS LETRAS:
    if CHUTE_ in PALAVRA_n:
        for P in range(0, Z_):
            POS_ = int(PALAVRA_n.index(CHUTE_))
            BACKS_n[POS_] = PALAVRA_n[POS_]
            PALAVRA_n[POS_] = '-'
        Llist(BACKS_n)
        ACERTOS_ -= Z_
        lin()
#   SE A LETRA ESTIVER ERRADA:
    else:
        if CHANCES_ > 1:
            CHANCES_ -= 1
            print(f'ERRADO. Chances: {CHANCES_}')
        else:
            print(f'Você Perdeu. A palavra era "{unidecode(PALAVRA_)}"')
            break
print(unidecode(PALAVRA_))