#Blibliotecas Kivy para o APP
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

#Extensão da classe número para o jogo
from numero import Numero

#Muda a cor do fundo
Window.clearcolor = (0.11, 0.17, 0.28)

#Tela inicial
class Home(Screen):
    def comecar(self, dificuldade): #Começa o jogo
        self.manager.current = "jogo" #vai para a tela de jogo

        jogo = self.manager.get_screen("jogo") #pega a configuração da tela de jogo
        jogo.escolherNumero(dificuldade) #executa a função da tela de jogo

# Tela do Jogo
class Jogo(Screen, Numero):
    sorteio = Numero() #Cria um objeto para o número

    def escolherNumero(self, dificuldade): #Função puxada pela tela Home
        self.sorteio.sortearNumero(dificuldade) #Sorteia o número do jogo de acordo com a dificuldade

        #Exibindo os dados na tela 
        self.ids.dica.text = f"{self.sorteio.menorNum} < ? < {self.sorteio.maiorNum}" #Exibe a dica
        self.ids.dificuldade.text = f"Dificuldade: {dificuldade}" #Exibe a dificuldade
        self.ids.tentativa.text = f"Tentativas: {self.sorteio.tentativas}"

    def palpite(self): #Função executada ao entrar com um número
        palpite = int(self.ids.palpite.text) #Pega o valor do inpout

        self.sorteio.tentativas += 1 #Muda o número de tentativas

        self.ids.tentativa.text = f"Tentativas: {self.sorteio.tentativas}" #Exibe as tentativas feitas

        if self.sorteio.tentativas >= 10:
            self.ids.dica.text = f"{self.sorteio.menorNum} < {self.sorteio.getNumero()} < {self.sorteio.maiorNum}" #Exibe a dica
            self.ids.feedback.text = f"AS TENTATIVAS ESGOTARAM! O NÚMERO SORTEADO ERA {self.sorteio.getNumero()}"

            Clock.schedule_once(self.voltar_menu, 3) #Após 5 seg de finalizar, o jogo volta para a home

        elif palpite < self.sorteio.getNumero():
            self.ids.feedback.text = f"O número sorteado é MAIOR que {palpite}!"

            if palpite > self.sorteio.menorNum: #Verifica se o palpite é maior que o menor numero citado para atualizar a dica do jogo
                self.sorteio.menorNum = palpite

            self.ids.dica.text = f"{self.sorteio.menorNum} < ? < {self.sorteio.maiorNum}" #Exibe a dica

        elif palpite > self.sorteio.getNumero():
            self.ids.feedback.text = f"O número sorteado é MENOR que {palpite}!"

            if palpite < self.sorteio.maiorNum: #Verifica se o palpite é menor que o maior numero citado para atualizar a dica do jogo
                self.sorteio.maiorNum = palpite

            self.ids.dica.text = f"{self.sorteio.menorNum} < ? < {self.sorteio.maiorNum}" #Exibe a dica

        else:
            self.ids.dica.text = f"{self.sorteio.menorNum} < {self.sorteio.getNumero()} < {self.sorteio.maiorNum}" #Exibe a dica
            self.ids.feedback.text = f"VOCÊ ACERTOU O NÙMERO ESCOLHIDO EM {self.sorteio.tentativas} TENTATIVAS!"

            Clock.schedule_once(self.voltar_menu, 3) #Após 5 seg de finalizar, o jogo volta para a home

    def voltar_menu(self, dt):
        self.manager.current = "home"

class Gerenciador(ScreenManager):
    pass

presentation = Builder.load_file("tela.kv")

class TelaApp(App):
    def build(self):
        #Configurações da tela
        self.title = "Adivinhe o Número" #Título
        self.icon = "img/Logo.png"#Ícone
        return presentation
        
if __name__ == '__main__':
    TelaApp().run()