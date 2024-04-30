#definir palavra secreta e como é aplicada
PalavraSecreta = 'Palavra'
PalavraSecretaLista = []
PalavraSecretaStatus = []
for letra in PalavraSecreta:
    PalavraSecretaLista.append(letra)
    PalavraSecretaStatus.append('_')
continues = True

while continues:
    #definir chute e tentativas
    dif = input('''Por favor escolha a dificuldade. 
                1 para fácil 
                2 para médio 
                3 para difícil''')
    Chute = input('chute?\n')
    if dif == '1':
        tentativas = 10
    elif dif == '2':
        tentativas = 5
    elif dif == '3':
        tentativas = 3

    while tentativas > 0:
        if Chute == letra:
            #acerto = PalavraSecretaLista[letra]
            #PalavraSecretaStatus[acerto] 
            print (PalavraSecretaStatus)
            print ('acerto')
        else:
            print ('falha')
            tentativas = tentativas -1
            print (f'{tentativas} restantes')
    if tentativas == 0:
        print ('Fim do jogo')
        confirmacao = input('''Tentar novamente?
                            1 para sim
                            0 para não 
                            ''')