from Contlist import contlist, contl

def Llist(list):
    for L in list:
        print(L, end='')
    print('')

#   INICIO, VARIAVEIS:
PALAVRA_ = str(input('Digite a palavra da forca: '))

CHANCES_ = 6
ACERTOS_ = int(len(PALAVRA_))

BACKS_n = []
PALAVRA_n = []


#   CRIANDO AS LISTAS:
for L_ in range(0, len(PALAVRA_)):
    BACKS_n.append('_')

for L_ in PALAVRA_:
    PALAVRA_n.append(L_)

Llist(BACKS_n)

#   CONDICIONANDO:  1
while ACERTOS_ != 0:
    CHUTE_ = str(input('Chute uma letra: '))[0]
    Z_ = contlist(PALAVRA_n, CHUTE_)

#       MAIS QUE UMA LETRA NA PALAVRA:
    if CHUTE_ in PALAVRA_n:
        if Z_ > 1:
            for P in range(0, Z_):
                POS_ = int(PALAVRA_n.index(CHUTE_))
                BACKS_n[POS_] = PALAVRA_n[POS_]
                PALAVRA_n[POS_] = '-'
            Llist(BACKS_n)
            ACERTOS_ -= Z_

#       APENAS UMA LETRA:
        else:
            POS_ = int(PALAVRA_n.index(CHUTE_))
            BACKS_n[POS_] = PALAVRA_n[POS_]
            PALAVRA_n[POS_] = '-'
            ACERTOS_ -= 1
            Llist(BACKS_n)

#
    else:
        if CHANCES_ > 1:
            CHANCES_ -= 1
            print(f'ERRADO. Chances: {CHANCES_}')
        else:
            print('Você Perdeu')
            break

