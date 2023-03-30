def Llist(list):
    for L in list:
        print(L, end='')
    print('')

#   INICIO:
PALAVRA_ = str(input('Digite a palavra da forca: '))
ACERTOS_ = len(PALAVRA_)
CHANCES_ = 6
BACKS_ = '_' * len(PALAVRA_)
BACKS_n = []

for B_ in BACKS_:
    BACKS_n.append(B_)

Llist(BACKS_n)
while ACERTOS_ != 0:
    CHUTE_ = str(input('Chute uma letra: '))[0]


#   CONDIÇÃO:

    if CHUTE_ in PALAVRA_:

        POS_ = int(PALAVRA_.find(CHUTE_))
        BACKS_n[POS_] = PALAVRA_[POS_]
        ACERTOS_ -= 1
        Llist(BACKS_n)
    else:
        if CHANCES_ > 1:
            CHANCES_ -= 1
            print(f'ERRADO. Chances: {CHANCES_}')
        else:
            print('Você Perdeu')
            break
