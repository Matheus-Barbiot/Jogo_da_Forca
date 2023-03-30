from Contlist import contlist, contl

def Llist(list):
    for L in list:
        print(L, end='')
    print('')

#   INICIO:
PALAVRA_ = str(input('Digite a palavra da forca: '))
CHANCES_ = 6
BACKS_ = '_' * len(PALAVRA_)
BACKS_n = []
PALAVRA_n = []
ACERTOS_ = int(len(PALAVRA_))
for B_ in BACKS_:
    BACKS_n.append(B_)

for l in PALAVRA_:
    PALAVRA_n.append(l)

Llist(BACKS_n)
while ACERTOS_ != 0:

    CHUTE_ = str(input('Chute uma letra: '))[0]
    Z_ = contlist(PALAVRA_n, CHUTE_)

    if CHUTE_ in PALAVRA_n:
        if Z_ > 1:
            for P in range(0, Z_):
                POS_ = int(PALAVRA_n.index(CHUTE_))
                BACKS_n[POS_] = PALAVRA_n[POS_]
                PALAVRA_n[POS_] = '-'
            Llist(BACKS_n)
            ACERTOS_ -= Z_

        else:
            POS_ = int(PALAVRA_n.index(CHUTE_))
            BACKS_n[POS_] = PALAVRA_n[POS_]
            PALAVRA_n[POS_] = '-'
            ACERTOS_ -= 1
            Llist(BACKS_n)
    else:
        if CHANCES_ > 1:
            CHANCES_ -= 1
            print(f'ERRADO. Chances: {CHANCES_}')
        else:
            print('Você Perdeu')
            break
#   CONDIÇÃO:
