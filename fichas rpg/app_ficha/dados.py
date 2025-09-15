import tkinter as tk
from tkinter import filedialog, messagebox
import json

class DadosFicha():
    def __init__(self):
        self.widgets = {}
        self.dados = {
            'informações':{},
            'atributos':{},
            'atributos_finais':{},
            'características':{},
            'características_finais':{},
            'danos':{},
            'perícias':{},
            'artefato':{},
            'magia':{}
        }
        
        self.informacoes = ['Nome', 'Level', 'Idade', 'Altura']
        self.caracteristicas = ['Ataque', 'Defesa', 'Vida', 'Sanidade']
        self.atributos = ['Força', 'Constituição','Vitalidade',
                    'Destreza','Agilidade','Mobilidade',
                    'Inteligência','Carisma','Aura']
        self.pericias = ['Arte marcial', 'Perícia com armas','Atletismo',
                    'Saúde','Acrobacia','Malandragem',
                    'Furtividade','Equilibrio','Habilidades artísticas',
                    'Blefar','Medicina','Conhecimento']
        
    def salvar_dados(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension='.json',
            filetypes=[('Arquivos JSON','*.json')],
            title='Salvar ficha.'
        )
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    dados_para_salvar = {
                        chave: {k: v.get() if isinstance(v, tk.StringVar) else v for k, v in secao.items()}
                        for chave, secao in self.dados.items()
                    }
                    json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
                    messagebox.showinfo('Sucesso','Sucesso, a ficha foi salva!')
            except Exception as e:
                messagebox.showerror('erro', f'erro ao salvar: {e}')

    def carregar_dados(self):
        caminho = filedialog.askopenfilename(
            defaultextension='.json',
            filetypes=[('Arquivos JSON','*.json')],
            title='Carregar ficha.'
        )
        if caminho:
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    dados_carregados = json.load(f)
                for secao, variavel in dados_carregados.items():
                    for chave, valor in variavel.items():
                        if secao in self.dados and chave in self.dados[secao]:
                            var = self.dados[secao][chave]
                            if isinstance(var, tk.StringVar):
                                var.set(valor)
                        if chave in self.widgets:
                            widget = self.widgets[chave]
                            widget.delete("1.0", "end")
                            widget.insert("1.0", valor)
                        
                        
                messagebox.showinfo("Sucesso", "Ficha restaurada!")
            except Exception as e:
                messagebox.showerror('erro', f'Erro ao carregar a ficha :{e}')