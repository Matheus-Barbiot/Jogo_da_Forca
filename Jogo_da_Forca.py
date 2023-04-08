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
        PALAVRA_LIST_[POS_] = '0'
def Chutes(): #Sistema de chute
    global TAMANHO_, CHUTE_
    while True:
        CHUTE_ = input('Chute uma letra: ').lower()
        if CHUTE_.isalpha() and len(CHUTE_) == 1 and not CHUTE_ in CHUTES_LIST_:
            TAMANHO_ = PALAVRA_LIST_.count(CHUTE_)
            CHUTES_LIST_.append(CHUTE_)
            break
        else:
            if CHUTE_ in CHUTES_LIST_:
                print('Você já chutou esta letra.')
            else:
                print('Digite uma letra válida.')
 
JOGO_ = True

#   TÍTULO:
while JOGO_ == True:
    print('')
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
    CHUTES_LIST_ = []
    COND_VITÓRIA_ = False


    #   CRIANDO AS LISTAS:
    for L_ in PALAVRA_ORIGINAL:
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

    while True:
        REINICIAR_ = str(input('Deseja reiniciar? [s/n] ')).lower()
        if REINICIAR_.isalpha() and len(REINICIAR_) == 1 and REINICIAR_ == 's' or REINICIAR_ == 'n':
            if REINICIAR_ == 's':
                break
            else:
                JOGO_ = False
                break
            
#   FINALIZAÇÃO:
linha('-')
print('Finalizado. obrigado por jogar!')
linha('-')