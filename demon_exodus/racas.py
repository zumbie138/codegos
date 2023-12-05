class Personagem:
    def __init__(self,nome_char,forca,agi,vit,int,car,level):
        self.nome = nome_char
        self.level = level
        self.forca = forca
        self.agilidade = agi
        self.vitalidade = vit
        self.inteligencia = int
        self.carisma = car
        self.level = level+1
        
class Humano(Personagem):
    def guerreiro(self):
        self.forca = 10 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 15 + self.vitalidade
        self.inteligencia = 5 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = (self.forca*(self.agilidade+(self.carisma/2)+(self.inteligencia/10)))/100
        self.defesa = (self.vitalidade*(self.agilidade+(self.forca/2)+(self.inteligencia/4)))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def mago(self):
        self.forca = 0 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 5 + self.vitalidade
        self.inteligencia = 20 + self.inteligencia
        self.carisma = 10 + self.carisma
        self.dano = (self.inteligencia*(self.carisma+(self.agilidade/2)+(self.forca/2)))/100
        self.defesa = (self.inteligencia*(self.vitalidade/2))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def clerigo(self):
        self.forca = 5 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 10 + self.vitalidade
        self.inteligencia = 10 + self.inteligencia
        self.carisma = 10 + self.carisma
        self.dano = (((self.carisma+self.inteligencia)/2)*(self.forca+self.agilidade))/100
        self.defesa = (((self.vitalidade+self.inteligencia/2))*(self.forca+self.carisma))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def ladrao(self):
        self.forca = 0 + self.forca
        self.agilidade = 15 + self.agilidade
        self.vitalidade = 0 + self.vitalidade
        self.inteligencia = 10 + self.inteligencia
        self.carisma = 15 + self.carisma
        self.dano = (self.agilidade*(self.forca+self.carisma+(self.inteligencia/2)))/100
        self.defesa = (self.agilidade*(self.vitalidade+(self.carisma/2)))/100
        self.vida = 100 + 100*self.vitalidade/100
        
class Elfo(Personagem):
    def ranger(self):
        self.forca = 5 + self.forca
        self.agilidade = 25 + self.agilidade
        self.vitalidade = 5 + self.vitalidade
        self.inteligencia = 10 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = (self.agilidade*(self.inteligencia+self.carisma))/100
        self.defesa = (self.vitalidade*(self.agilidade+(self.forca/2)))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def feiticeiro(self):
        self.forca = 0 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 0 + self.vitalidade
        self.inteligencia = 30 + self.inteligencia
        self.carisma = 15 + self.carisma
        self.dano = (self.inteligencia*(self.inteligencia+self.carisma))/100
        self.defesa = (self.carisma*(self.vitalidade+self.agilidade))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def druida(self):
        self.forca = 10 + self.forca
        self.agilidade = 10 + self.agilidade
        self.vitalidade = 10 + self.vitalidade
        self.inteligencia = 10 + self.inteligencia
        self.carisma = 10 + self.carisma
        self.dano = (((self.inteligencia+self.carisma)/2)*((self.forca/2)+(self.agilidade/2)))/100
        self.defesa = ((self.vitalidade+self.carisma)*(self.forca+self.agilidade))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def bardo(self):
        self.forca = 0 + self.forca
        self.agilidade = 0 + self.agilidade
        self.vitalidade = 0 + self.vitalidade
        self.inteligencia = 20 + self.inteligencia
        self.carisma = 30 + self.carisma
        self.dano = ((()))/100
        self.defesa = ((()))/100
        self.vida = 100 + 100*self.vitalidade/100
        
class Orc(Personagem):
    def barbaro(self):
        self.forca = 30 + self.forca
        self.agilidade = 20 + self.agilidade
        self.vitalidade = 10 + self.vitalidade
        self.inteligencia = 0 + self.inteligencia
        self.carisma = 0 + self.carisma
        self.dano = (self.forca*(self.forca+self.agilidade))/100
        self.defesa = (self.vitalidade*(self.forca+self.agilidade))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def bruxo(self):
        self.forca = 25 + self.forca
        self.agilidade = 0 + self.agilidade
        self.vitalidade = 15 + self.vitalidade
        self.inteligencia = 10 + self.inteligencia
        self.carisma = 10 + self.carisma
        self.dano = (self.inteligencia*(self.agilidade+self.forca))/100
        self.defesa = (self.vitalidade*(self.agilidade/2))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def shaman(self):
        self.forca = 20 + self.forca
        self.agilidade = 10 + self.agilidade
        self.vitalidade = 10 + self.vitalidade
        self.inteligencia = 10 + self.inteligencia
        self.carisma = 10 + self.carisma
        self.dano = (((self.inteligencia+self.carisma)/2)*((self.forca/2)+(self.agilidade/2)))/100
        self.defesa = ((self.vitalidade+self.carisma)*(self.forca+self.agilidade))/100
        self.vida = 100 + 100*self.vitalidade/100
        
    def saqueador(self):
        self.forca = 30 + self.forca
        self.agilidade = 20 + self.agilidade
        self.vitalidade = 10 + self.vitalidade
        self.inteligencia = 0 + self.inteligencia
        self.carisma = 0 + self.carisma
        self.dano = ((()))/100
        self.defesa = ((()))/100
        self.vida = 100 + 100*self.vitalidade/100