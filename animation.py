import pygame
import os
import sys

pygame.init()

largura, altura = 900, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Animação Pygame")

diretorio_frames = 'C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation'
imagens = []
for i in range(45):
    caminho_imagem = os.path.join(diretorio_frames, f"frame {i}.png")
    imagem = pygame.image.load(caminho_imagem)
    imagens.append(imagem)

frame_atual = 0
taxa_atualizacao = 3 

clock = pygame.time.Clock()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((255, 255, 255))
    tela.blit(imagens[frame_atual], (0, 0))
    pygame.display.flip()
    clock.tick(taxa_atualizacao)
    frame_atual = (frame_atual + 1) % len(imagens)

pygame.quit()
sys.exit()