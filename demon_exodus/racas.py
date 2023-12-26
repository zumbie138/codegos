class Personagem:
    def __init__(self,nome_char,forca,agi,vit,int,car,level):
        self.nome = nome_char
        self.forca = forca
        self.agilidade = agi
        self.vitalidade = vit
        self.inteligencia = int
        self.carisma = car
        self.level = level + 1
        self.equipamentos = {
            'cabeça':None,
            'torso':None,
            'cintura':None,
            'pernas':None,
            'mao_direita':None,
            'mao_esquerda':None,
            'pés':None,
            'mãos':None,
            'dedo1':None,
            'dedo2':None,
            'pescoço':None,
        }
        self.inventario = {}
        
    def equipar_item(self):
        self.item = 0
        
class Humano(Personagem):
    def guerreiro(self):
        self.forca = 4 + self.forca
        self.agilidade = 3 + self.agilidade
        self.vitalidade = 5 + self.vitalidade
        self.inteligencia = 0.5 + self.inteligencia
        self.carisma = 0.5 + self.carisma
        self.dano = (self.forca*(self.agilidade+(self.carisma/2)+(self.inteligencia/10)))/10
        self.defesa = (self.vitalidade*(self.agilidade+(self.forca/2)+(self.inteligencia/4)))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def mago(self):
        self.forca = 1 + self.forca
        self.agilidade = 1 + self.agilidade
        self.vitalidade = 1 + self.vitalidade
        self.inteligencia = 5 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = (self.inteligencia*(self.carisma+(self.agilidade/2)+(self.forca/2)))/10
        self.defesa = (self.inteligencia*(self.vitalidade/2))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def clerigo(self):
        self.forca = 1 + self.forca
        self.agilidade = 1 + self.agilidade
        self.vitalidade = 2 + self.vitalidade
        self.inteligencia = 4 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = (((self.carisma+self.inteligencia)/2)*(self.forca+self.agilidade))/10
        self.defesa = (((self.vitalidade+self.inteligencia/2))*(self.forca+self.carisma))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def ladrao(self):
        self.forca = 1 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 1 + self.vitalidade
        self.inteligencia = 1 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = (self.agilidade*(self.forca+self.carisma+(self.inteligencia/2)))/10
        self.defesa = (self.agilidade*(self.vitalidade+(self.carisma/2)))/10
        self.vida = 100 + 100*self.vitalidade/100
        
class Elfo(Personagem):
    def ranger(self):
        self.forca = 5 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 1 + self.vitalidade
        self.inteligencia = 1 + self.inteligencia
        self.carisma = 1 + self.carisma
        self.dano = (self.agilidade*(self.inteligencia+self.carisma))/10
        self.defesa = (self.vitalidade*(self.agilidade+(self.forca/2)))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def feiticeiro(self):
        self.forca = 1 + self.forca
        self.agilidade = 2 + self.agilidade
        self.vitalidade = 1 + self.vitalidade
        self.inteligencia = 5 + self.inteligencia
        self.carisma = 4 + self.carisma
        self.dano = (self.inteligencia*(self.inteligencia+self.carisma))/10
        self.defesa = (self.carisma*(self.vitalidade+self.agilidade))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def druida(self):
        self.forca = 1 + self.forca
        self.agilidade = 2 + self.agilidade
        self.vitalidade = 2 + self.vitalidade
        self.inteligencia = 3 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = (((self.inteligencia+self.carisma)/2)*((self.forca/2)+(self.agilidade/2)))/10
        self.defesa = ((self.vitalidade+self.carisma)*(self.forca+self.agilidade))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def bardo(self):
        self.forca = 0.5 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 0.5 + self.vitalidade
        self.inteligencia = 2 + self.inteligencia
        self.carisma = 5 + self.carisma
        self.dano = ((()))/10
        self.defesa = ((()))/100
        self.vida = 100 + 100*self.vitalidade/100
        
class Orc(Personagem):
    def barbaro(self):
        self.forca = 5 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 2 + self.vitalidade
        self.inteligencia = 0.5 + self.inteligencia
        self.carisma = 0.5 + self.carisma
        self.dano = (self.forca*(self.forca+self.agilidade))/10
        self.defesa = (self.vitalidade*(self.forca+self.agilidade))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def bruxo(self):
        self.forca = 2 + self.forca
        self.agilidade = 1 + self.agilidade
        self.vitalidade = 2 + self.vitalidade
        self.inteligencia = 5 + self.inteligencia
        self.carisma = 3 + self.carisma
        self.dano = (self.inteligencia*(self.agilidade+self.forca))/10
        self.defesa = (self.vitalidade*(self.agilidade/2))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def shaman(self):
        self.forca = 2 + self.forca
        self.agilidade = 1 + self.agilidade
        self.vitalidade = 2 + self.vitalidade
        self.inteligencia = 4 + self.inteligencia
        self.carisma = 4 + self.carisma
        self.dano = (((self.inteligencia+self.carisma)/2)*((self.forca/2)+(self.agilidade/2)))/10
        self.defesa = ((self.vitalidade+self.carisma)*(self.forca+self.agilidade))/10
        self.vida = 100 + 100*self.vitalidade/100
        
    def saqueador(self):
        self.forca = 5 + self.forca
        self.agilidade = 5 + self.agilidade
        self.vitalidade = 1 + self.vitalidade
        self.inteligencia = 1 + self.inteligencia
        self.carisma = 1 + self.carisma
        self.dano = ((()))/100
        self.defesa = ((()))/100
        self.vida = 100 + 100*self.vitalidade/100