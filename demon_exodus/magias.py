class Magias:
    def __init__(self,level,forca,agi,vit,int,car,dano,defesa):
        self.level = level
        self.foca = forca
        self.agilidade = agi
        self.vitalidade = vit
        self.inteligencia = int
        self.carisma = car
        self.dano = dano
        self.defesa = defesa
        
    def curar_minima(self):
        self.nome = 'Curar feridas leves'
        self.fator_cura = 3 + self.inteligencia + self.vitalidade/2