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
        self.dano_c = self.agilidade_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.ouro = randint(0,1)
        self.experiencia_c = randint(1,5)
        self.espolios = {'pelo de rato':20,'anel quebrado':1,'restos de comida':10,'queijo':15}
        
    def cobra(self):
        self.forca_c = 0
        self.agilidade_c = 40
        self.vitalidade_c = 0
        self.inteligencia_c = 0
        self.carisma_c = 5
        self.vida_c = 30
        self.vida_c_t = 30
        self.dano_c = self.agilidade_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(1,5)
        self.espolios = {'presa de cobra':20,'escama de cobra':15,'colar da serpente':1}
        
    def morcego(self):
        self.forca_c = 0
        self.agilidade_c = 40
        self.vitalidade_c = 5
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 35
        self.vida_c_t = 35
        self.dano_c = self.agilidade_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(1,6)
        self.espolios = {'asa de morcego':20,'dente vampirico':15,'adaga enferrujada':1}
        
    def lobo(self):
        self.forca_c = 10
        self.agilidade_c = 5
        self.vitalidade_c = 10
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 50
        self.vida_c_t = 50
        self.dano_c = self.forca_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(2,6)
        self.espolios = {'presa de lobo':20,'garra de lobo':15,'espada enferrujada':1}
        
    def urso(self):
        self.forca_c = 20
        self.agilidade_c = 5
        self.vitalidade_c = 20
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 90
        self.vida_c_t = 90
        self.dano_c = self.forca_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(2,7)
        self.espolios = {'couro medio':20,'garra de urso':15,'escudo enferrujado':1}
        
    def troll(self):
        self.forca_c = 10
        self.agilidade_c = 10
        self.vitalidade_c = 10
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 110
        self.vida_c_t = 110
        self.dano_c = self.forca_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(3,8)
        self.espolios = {'dedo de troll':20,'cajado':15,'calsa de couro':1}
        
    def rato_zumbi(self):
        self.forca_c = 5
        self.agilidade_c = 20
        self.vitalidade_c = 10
        self.inteligencia_c = 0
        self.carisma_c = 0
        self.vida_c = 40
        self.vida_c_t = 40
        self.dano_c = self.agilidade_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(2,5)
        self.espolios = {'carne podre':20,'ossos':15,'botas':1}
        
    def aranha(self):
        self.forca_c = 5
        self.agilidade_c = 40
        self.vitalidade_c = 5
        self.inteligencia_c = 5
        self.carisma_c = 0
        self.vida_c = 30
        self.vida_c_t = 30
        self.dano_c = self.agilidade_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(2,5)
        self.espolios = {'veneno':20,'olhos de aranha':15,'diamante':1}
        
    def caveira(self):
        self.forca_c = 20
        self.agilidade_c = 20
        self.vitalidade_c = 20
        self.inteligencia_c = 5
        self.carisma_c = 5
        self.vida_c = 150
        self.vida_c_t = 150
        self.dano_c = self.forca_c*((self.forca_c/2+self.agilidade_c/2))/100
        self.defesa_c = self.vitalidade_c*((self.forca_c+self.agilidade_c))/100
        self.experiencia_c = randint(4,9)
        self.espolios = {'cranio':20,'ossos':15,'arco':1}
    