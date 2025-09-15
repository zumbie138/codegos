import tkinter as tk
from widgets import CriadorDeWidgets

class PaginaDois(tk.Frame, CriadorDeWidgets):
    def __init__(self, app, dados_ficha):
        super().__init__(app, bg='Black')
        self.dados_ficha = dados_ficha
        self.app = app
        self.aplicar_pagina_dois()
    
    def criar_campos_textos(self, i:int, linha_label:int, linha_text:int, coluna:int, dado:str):
        chave = f'{dado} {i+1}'
        self.criar_label(
            texto=chave.capitalize(), tamanho_texto=11, 
            cor_fg='red', cor_bg='#0C0101', 
            linha=linha_label, coluna=coluna, tamanho_coluna=1,
            tipo_sticky='w'
        )
        widget = self.criar_text(
            altura=6,
            largura=80,
            linha=linha_text,
            coluna=coluna
        )
        widget.nome = chave
        widget.secao = dado
        self.dados_ficha.widgets[chave] = widget
        
        widget.bind('<KeyRelease>', lambda event, c=widget, k=dado, t=chave:self.armazenar_texto(c, k, t))

    
    def armazenar_texto(self, widget_text, tipo_dado, chave):
        conteudo = widget_text.get('1.0', 'end-1c')
        self.dados_ficha.dados[tipo_dado][chave] = conteudo
        
    def aplicar_pagina_dois(self):
        #label dos artefatos posiçao 0 coluna 0
        self.criar_label(
            texto='Artefatos',
            tamanho_texto=20,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=0,
            coluna=0,
            tamanho_coluna=1,
            tipo_sticky='w'
        )
        #posicionar texts dos artefatos posição 1 ate 12 coluna 10
        for i in range(3):
            linha_label = i*4 + 1
            linha_text = linha_label + 1
            self.criar_campos_textos(i, linha_label, linha_text, 0,'artefato')
        
        #espaço vazio de coluna 
        for i in range(21):
            self.criar_label(
                texto='',
                tamanho_texto=1,
                cor_fg=None,
                cor_bg='red',
                linha=i,
                coluna=1,
                tamanho_coluna=1,
                tipo_sticky='e'
            )
        
        #label das magias posiçao 0 coluna 2
        self.criar_label(
            texto='Magias',
            tamanho_texto=20,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=0,
            coluna=2,
            tamanho_coluna=1,
            tipo_sticky='w'
        )
        #posicionar texts das magias posiçao 1 ate 20 coluna 2
        for i in range(5):
            linha_label = i*4 + 1
            linha_text = linha_label + 1
            self.criar_campos_textos(i, linha_label, linha_text, 2,'magia')
            
        self.criar_botao(
            texto='SALVAR',
            comando=self.dados_ficha.salvar_dados,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=13,
            coluna=0
        )
        self.criar_botao(
            texto='CARREGAR',
            comando=self.dados_ficha.carregar_dados,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=14,
            coluna=0
        )
        self.criar_botao(
            texto='Página anterior.',
            comando=lambda: self.app.mostrar_pagina(self.app.pagina_um),
            cor_fg='black',
            cor_bg='#AA0000',
            linha=19,
            coluna=0
        )