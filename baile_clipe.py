import pygame
import os
import sys

dir_prefacio='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\prefacio'
dir_intro1='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\intro_1'
dir_intro2='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\intro_2'
dir_verso1='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\verso_1'
dir_verso2='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\verso_2'
dir_ponte='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\ponte'
dir_refrao='C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\refrao'

def prefacio():
    imagens_v,len_v=importar_imagens(dir_prefacio)
    chamar_animacao(imagens_v,len_v)
    intro_1()

def intro_1():
    imagens_v,len_v=importar_imagens(dir_intro1)
    chamar_animacao(imagens_v,len_v)
    intro_2()
    
def intro_2():
    imagens_v,len_v=importar_imagens(dir_intro2)
    chamar_animacao(imagens_v,len_v)
    verso_1()
    
def verso_1():
    imagens_v,len_v=importar_imagens(dir_verso1)
    chamar_animacao(imagens_v,len_v)
    ponte(1)

def ponte(aux):
    imagens_v,len_v=importar_imagens(dir_ponte)
    chamar_animacao(imagens_v,len_v)
    match aux:
        case 1:
            verso_2()
        case 2:
            refrão()
    
def verso_2():
    imagens_v,len_v=importar_imagens(dir_verso2)
    chamar_animacao(imagens_v,len_v)
    ponte(2)

def refrão():
    imagens_v,len_v=importar_imagens(dir_refrao)
    chamar_animacao(imagens_v,len_v)
    
def chamar_animacao(imagens,num_frame):
    pygame.init()
    largura, altura = 900, 1000
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Animação Pygame")
    taxa_atualizacao = 3 
    clock = pygame.time.Clock()
    for frame in range(num_frame):
        tela.fill((255, 255, 255))
        tela.blit(imagens[frame], (0, 0))
        pygame.display.flip()
        clock.tick(taxa_atualizacao)
    
def importar_imagens(diretorio_frames):
    imagens = []
    vetor = os.listdir(diretorio_frames)
    len_vetor=int(len(vetor))
    for i in range(len_vetor):
        caminho_imagem = os.path.join(diretorio_frames, f"f{i}.png")
        imagem = pygame.image.load(caminho_imagem)
        imagens.append(imagem)
    return imagens,len_vetor

prefacio()
pygame.quit()
sys.exit()