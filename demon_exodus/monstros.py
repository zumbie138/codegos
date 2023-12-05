from random import randint
class Criaturas:
    def __init__(self):
        nome = ''

    def rato(self):
        self.forca_c = 0
        self.agilidade_c = 40
        self.vitalidade_c = 0
        self.inteligencia_c = 0
        self.carisma_c = 0
        self.vida_c = 20
        self.vida_c_t = 20
        self.dano_c = self.agilidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.ouro = randint(0,1)
        self.experiencia_c = randint(1,5)
        
    def cobra(self):
        self.forca_c = 0
        self.agilidade_c = 40
        self.vitalidade_c = 0
        self.inteligencia_c = 0
        self.carisma_c = 5
        self.vida_c = 30
        self.vida_c_t = 30
        self.dano_c = self.agilidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(1,5)
        
    def morcego(self):
        self.forca_c = 0
        self.agilidade_c = 40
        self.vitalidade_c = 5
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 35
        self.vida_c_t = 35
        self.dano_c = self.agilidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(1,6)
        
    def lobo(self):
        self.forca_c = 10
        self.agilidade_c = 5
        self.vitalidade_c = 10
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 50
        self.vida_c_t = 50
        self.dano_c = self.forca_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(2,6)
        
    def urso(self):
        self.forca_c = 20
        self.agilidade_c = 5
        self.vitalidade_c = 20
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 90
        self.vida_c_t = 90
        self.dano_c = self.forca_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(2,7)
        
    def troll(self):
        self.forca_c = 10
        self.agilidade_c = 10
        self.vitalidade_c = 10
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 110
        self.vida_c_t = 110
        self.dano_c = self.forca_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(3,8)
        
    def rato_zumbi(self):
        self.forca_c = 5
        self.agilidade_c = 20
        self.vitalidade_c = 10
        self.inteligencia_c = 0
        self.carisma_c = 0
        self.vida_c = 40
        self.vida_c_t = 40
        self.dano_c = self.agilidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(2,5)
        
    def aranha(self):
        self.forca_c = 5
        self.agilidade_c = 40
        self.vitalidade_c = 5
        self.inteligencia_c = 5
        self.carisma_c = 0
        self.vida_c = 30
        self.vida_c_t = 30
        self.dano_c = self.agilidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(2,5)
        
    def caveira(self):
        self.forca_c = 20
        self.agilidade_c = 20
        self.vitalidade_c = 20
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 150
        self.vida_c_t = 150
        self.dano_c = self.forca_c*((self.forca_c+self.agilidade_c)/10)/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c)/10)/100
        self.experiencia_c = randint(4,9)
    