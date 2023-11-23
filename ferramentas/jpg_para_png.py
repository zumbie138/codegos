from PIL import Image
import os

def converter_jpg_para_png(caminho_pasta_origem, caminho_pasta_destino):
    for arquivo in os.listdir(caminho_pasta_origem):
        if arquivo.lower().endswith('.jpg'):
            caminho_arquivo_origem = os.path.join(caminho_pasta_origem, arquivo)
            nome_arquivo_sem_extensao = os.path.splitext(arquivo)[0]
            caminho_arquivo_destino = os.path.join(caminho_pasta_destino, f'{nome_arquivo_sem_extensao}.png')
            
            imagem = Image.open(caminho_arquivo_origem)
            imagem.save(caminho_arquivo_destino, 'PNG')
            print(f"Arquivo {caminho_arquivo_origem} convertido para {caminho_arquivo_destino}")

caminho_pasta_origem = 'C:\\Users\\Zhafyr\\Desktop\\desenhos\\pata desenhos\\Baile cripe\\Nova pasta\\animation\\refrao'

converter_jpg_para_png(caminho_pasta_origem, caminho_pasta_origem)