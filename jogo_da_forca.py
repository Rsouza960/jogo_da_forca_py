import random

# Jogo da forca utilizando POO

#palco da forca
palco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']

#classe

class Forca:
    #metodo construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []



    #metodo para adivinhar a letra
    def advinha(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    #metodo para verificar se o jogo terminou
    def forca_acabou(self):
        if self.forca_venceu() or (len(self.letras_erradas)>=5):
            return True
        return False

    #metodo para verificar se o jogador venceu
    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    #metodo para não mostrar a letra no palco
    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '_'
            else:
                status += letra
        return status
    
    #metodo para checar o status do jogo e imprimir o palco na tela
    def mostrar_status_jogo(self):
        print('\n===== Jogo da Forca======')
        print(palco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print('\n letras erradas: ')
        for letra in self.letras_erradas:
            print(letra,)
        print('\n letras corretas: ')
        for letra in self.letras_certas:
            print(letra,)

#funcao para ler uma palavra de forma aleatória do banco de palavras

def palavra_aleatoria():
    with open("palavras.txt", 'rt') as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

#funcao Main - Execução do programa


def main():
    #objeto
    jogo = Forca(palavra_aleatoria())

    #enquanto o jogo nao tiver terminado, mostrar do status,
    #solicita uma letra e faz a leitura do caracter
    while not jogo.forca_acabou():
        jogo.mostrar_status_jogo()
        letra_escolhida = input('\nDigite uma letra: ')
        jogo.advinha(letra_escolhida)

    #verifica o status do jogo
    jogo.mostrar_status_jogo()

    #de acordo com o status, imprime mensagem na tela para o usuario
    if jogo.forca_venceu():
        print('\n parabens, voce ganhou!')
    else:
        print('\n Fim de jogo, você perdeu')
        print('\n A palavra era' + jogo.palavra)

    print('\n Foi bom jogar com você!')

#Executa o programa
if __name__ == '__main__':
    main()