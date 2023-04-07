#   BIBILIOTÉCAS:
import random
from unidecode import unidecode


#   FUNÇÕES:
def linha(l='=', n=50): #Cria uma linha para separar
    print(l * n)
def Format_Letras(): #Formata os _ para as letras e etc
    POS_ = -1
    for P in range(0, TAMANHO_):
        POS_ = int(PALAVRA_LIST_.index(CHUTE_, POS_+1))
        BACKS_LIST_[POS_] = PALAVRA_LIST_[POS_]
        PALAVRA_LIST_[POS_] = '-'
def Chutes(): #Sistema de chute
    global TAMANHO_, CHUTE_
    if ACERTOS_ == 1:
        CHUTE_ = str(input('Chance para chutar a PALAVRA: ')).lower()
    else:
        while True:
            CHUTE_ = str(input('Chute uma letra: ')).lower().strip()[0]
            if len(CHUTE_) > 0:
                TAMANHO_ = PALAVRA_LIST_.count(CHUTE_)
                break
            else:
                print('Digite uma letra válida.')
 

#   TÍTULO:
linha()
print(f'{"JOGO DA FORCA":^50}')
linha()


#   INICIO, VARIAVEIS:
try: 
    with open('Palavras.txt', 'r', encoding='utf-8') as A:
        PALAVRAS_LIST_ = A.read().splitlines()

except FileNotFoundError:
    print('Palavra não encontrada. Tente novamente. . .')


PALAVRA_ORIGINAL = random.choice(PALAVRAS_LIST_).lower()
PALAVRA_ = unidecode(PALAVRA_ORIGINAL)
CHANCES_ = 6
ACERTOS_ = len(PALAVRA_)
BACKS_LIST_ = []
PALAVRA_LIST_ = []
COND_VITÓRIA_ = False


#   CRIANDO AS LISTAS:
for L_ in PALAVRA_:
    PALAVRA_LIST_.append(L_)
    if L_ != ' ':
        BACKS_LIST_.append('_')
    else:
        BACKS_LIST_.append(' ')
        ACERTOS_ -= 1


BACKS_STRING = ' '.join(BACKS_LIST_)
print(f'{BACKS_STRING:^50}')


#   LOOP PRINCIPAL:
while True:
    linha('-')
    Chutes()
    linha('-')


#   TERMINANDO A PALAVRA:
    if ACERTOS_ == 1:
        if CHUTE_ == PALAVRA_:
                COND_VITÓRIA_ = True
                break
        else:
            BACKS_STRING = ' '.join(BACKS_LIST_)
            print(f'{BACKS_STRING:^50}')


#   COLOCANDO AS LETRAS:
    if CHUTE_ in PALAVRA_LIST_:
        Format_Letras()
        ACERTOS_ -= TAMANHO_
        BACKS_STRING = ' '.join(BACKS_LIST_)
        print(f'{BACKS_STRING:^50}')


#   SE A LETRA ESTIVER ERRADA:
    else:
        if CHANCES_ > 1:
            CHANCES_ -= 1
            linha()
            print(f'Você errou. Chances restantes: {CHANCES_}')
            linha()
            linha('-')
            BACKS_STRING = ' '.join(BACKS_LIST_)
            print(f'{BACKS_STRING:^50}')
        else:
            break


#   CONDIÇÃO DE VITÓRIA:
if COND_VITÓRIA_ != True:
    linha()
    print(f'Você perdeu. A palavra era {PALAVRA_ORIGINAL}')
    linha()
else:
    linha()
    print(f'Parabéns, você acertou. A palavra é "{PALAVRA_ORIGINAL}"')
    linha()
