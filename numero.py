import random

class Numero(): #Classe que armazena os dados da partida
    def __init__(self):
        self.__numero = 0
        self.menorNum = 0
        self.maiorNum = 0
        self.tentativas = 0

    def sortearNumero(self, dificuldade): #Função que sorteia o número e reseta a partida

        #Resetando a partida
        self.menorNum = 1
        self.tentativas = 0

        if dificuldade == "Fácil":
            self.__numero = random.randint(1, 25) #Sorteia o número
            self.maiorNum = 25 #Seleciona o maior número de acordo com a dificuldade

        elif dificuldade == "Médio":
            self.__numero = random.randint(1, 60)
            self.maiorNum = 60

        else:
            self.__numero = random.randint(1, 100)
            self.maiorNum = 100

    
    def getNumero(self):
        return self.__numero