import Banco_palavras as bp # Importação da biblioteca que criei para guardar as palavras
from random import choice # Função para escolher as palavras aleatoriamente

def main():
    # Explica o jogo ao usuario
    tentativa = 10
    print('\n\nSeja bem vindo ao jogo das palavras!')
    print('O jogo é bem simples, é nescessario acertar a palavra corretamente.')
    print('O jogo dará dicas somente se você acertar a posição exata da letra.')
    print('OBS: Não se esqueça dos acentos, o jogo somente dará dicas se estiver com eles corretamente.')
    print('Você tem somente', tentativa, 'tentativas por rodada\n')

    aux = 1
    while aux != '':
        rodada(tentativa)
        aux = input('\nAperte enter para fechar ou qualquer digite coisa para continuar: ')
        aux.lower()
    
    # Fechar o app caso o usuario aperte um enter
    exit()

def rodada(tentativa):
    #Função para deixar o jogo dinamico e o usuario conseguir jogar sem ter que ficar abrindo jogo novamente

    # Escolhe randomicamente a palavra e seus respectivos elementos, como o tamanho
    palavras = bp.palavras
    escolhe_qtd_letras = choice(palavras)
    palavra_escolhida = choice(escolhe_qtd_letras)
    tamanho_palavra = len(palavra_escolhida)

    print('\nNessa rodada iremos jogar com uma palavra de', tamanho_palavra, 'letras.', end='\t' )
    linhas(tamanho_palavra)

    print('\n')

    # Chama a função que faz o processo do jogo que retorna valores booleanos caso ele consiga ou nao ganhar
    if tentativas(tamanho_palavra, palavra_escolhida, tentativa):
        print('Parabens você conseguiu! a palavra correta era:', palavra_escolhida)
    else:
       print('\n:( poxa que pena, tente novamente! Você consegue! A palavra correta era:', palavra_escolhida)

    
def tentativas(tamanho_palavra, palavra_escolhida, tentativas):
    # Faz o usuario escrever certo, limitando-o pelas tentativa
    # Essa é a função responsavel pelo funcionamento vital do programa

    palavra_usuario = recebe_palavra_usuario(tamanho_palavra)
    letras_certas = verifica_palavra_usuario(palavra_escolhida, palavra_usuario)


    if letras_certas[:] == palavra_escolhida[:]:
        return True
    else:
        aux = 1
        while aux < tentativas:
            escreve_tentativa(letras_certas)
            palavra_usuario = recebe_palavra_usuario(tamanho_palavra)
            letras_certas = verifica_palavra_usuario(palavra_escolhida, palavra_usuario)
            if letras_certas[:] == palavra_escolhida[:]:
                return True
            else: 
                aux += 1
    return False



# A partir daqui são funções auxiliares para o processo ter funções pequenas para facil compreenção e manutenção

def linhas(tamanho_palavra):
    # Escreve a quantidade de letras da palavra inicial 

    for i in range(tamanho_palavra - 1):
        print('_', end=' ')
    print('_')


def recebe_palavra_usuario(tamanho_palavra):
    # Recebe e trata a palavra do usuario

    palavra_usuario = input("\nTentativa: ")

    while(len(palavra_usuario) != tamanho_palavra):
        print('\nAviso digite uma palavra com', tamanho_palavra, 'letras')
        palavra_usuario = input("Tentativa: ")
    
    return palavra_usuario.lower()


def verifica_palavra_usuario(palavra_escolhida, palavra_usuario):
    # Verifica se a palavra do usuario é identica a palavra do sistema

    letras_certas = []

    if palavra_escolhida[:] == palavra_usuario[:]:
        return palavra_escolhida
    else:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == palavra_usuario[i]:
                letras_certas.append(palavra_usuario[i])
            else:
                letras_certas.append('_')

    return letras_certas


def escreve_tentativa(letras_certas):
    # Escreve a tentativa do usuario tratando o vetor recebido

    for i in range(len(letras_certas) - 1):
        print(letras_certas[i], end=' ')
    print(letras_certas[-1])

# faz o jogo rodar
main()