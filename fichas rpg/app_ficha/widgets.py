import tkinter as tk
from tkinter import ttk

class CriadorDeWidgets:
    def criar_entry(self,str_dict:str, str_estado:str,tamanho:int,linha:int,coluna:int,tipo_sticky:str):
        tk.Entry(
            self, 
            textvariable=str_dict, 
            state=str_estado, 
            width=tamanho
            ).grid(
                row=linha,
                column=coluna,
                sticky=tipo_sticky
                )
            
    def criar_label(self,texto:str, tamanho_texto:int, cor_fg:str, cor_bg:str, linha:int, coluna:int, tamanho_coluna:int, tipo_sticky:str):
        tk.Label(
        self, 
        text=texto, 
        font=('Cloister Black Light', tamanho_texto),
        fg=cor_fg,
        bg=cor_bg
        ).grid(
            row=linha, 
            column=coluna, 
            columnspan=tamanho_coluna,
            sticky=tipo_sticky
            )
        
    def criar_combobox(self, text:str, lista_values:list, tamanho_font:int, tamanho_width:int, linha:int, coluna:int):
        ttk.Combobox(
            self, 
            textvariable=text, 
            values=lista_values, 
            font=('Cloister Black Light',tamanho_font), 
            width=tamanho_width
            ).grid(row=linha, column=coluna)
        
    def criar_botao(self,texto:str,comando, cor_fg:str, cor_bg:str, linha:int, coluna:int):
        tk.Button(
            self,
            text=texto, 
            command=comando,
            fg=cor_fg,
            bg=cor_bg
            ).grid(row=linha, column=coluna
        )
 
    def criar_text(self,altura:int, largura:int, linha:int, coluna:int):
        text = tk.Text(
            self,
            height=altura,
            width=largura
        )
        text.grid(row=linha,column=coluna)
        return text