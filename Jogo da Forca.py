#   INICIO:
PALAVRA_ = str(input('Digite a palavra da forca: '))
CHANCES_ = 6
BACKS_ = '_' * len(PALAVRA_)
BACKS_n = []

for B_ in BACKS_:
    BACKS_n.append(B_)

print(BACKS_n)

CHUTE_ = str(input('Chute uma letra: '))[0]


#   CONDIÇÃO:
if CHUTE_ in PALAVRA_:

    POS_ = int(PALAVRA_.find(CHUTE_))
    BACKS_n[POS_] = PALAVRA_[POS_]

    print(POS_)
    print(BACKS_n)
else:
    CHANCES_ -= 1
    print(f'ERRADO. Chanches: {CHANCES_}')
