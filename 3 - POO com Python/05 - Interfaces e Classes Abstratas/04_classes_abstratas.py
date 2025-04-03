from abc import ABC, abstractmethod

class Controle_Remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
class Controle_TV(Controle_Remoto):
    def ligar(self):
        print("Ligando a TV...")

    def desligar(self):
        print("Desligando a TV...")
        
class Controle_ArCondicionado(Controle_Remoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
    
    def desligar(self):
        print("Desligando o Ar Condicionado...")

controle = Controle_TV()
controle.ligar()
controle.desligar()

controle = Controle_ArCondicionado()
controle.ligar()
controle.desligar()