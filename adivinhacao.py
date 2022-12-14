import random

def jogar():
    print ('********************************')
    print ('Bem vindo ao jogo de adivinhação')
    print ('********************************')

    numero_secreto = random.randrange(1,101)

    print('Qual nível de dificuldade você deseja?')
    print('(1) Fácil, (2) Médio, (3) Difícil')
    nivel = int(input('Defina um nível: '))
    pontos = 1000

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2 ):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print ('tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input('Digíte o seu número entre 1 a 100: ')
        print ('Você digitou ', chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print ('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print ('Você errou! O seu chute foi maior do que o número secreto.')
            elif  (chute < numero_secreto):
                print ('Você errou! O seu chute foi menor do que o número secreto.')
            pontos_pedidos = abs((numero_secreto - chute))
            pontos = pontos - pontos_pedidos

    print ('Fim do jogo')

if (__name__ == "__main__"):
    jogar()