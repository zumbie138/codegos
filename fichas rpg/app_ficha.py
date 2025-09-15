import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import json

class AppFichaDeMortis(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ficha de RPG De Mortis')
        self.configure(bg='Black')

        self.pagina_um = PaginaUm(self)
        self.pagina_dois = PaginaDois(self)
        self.pagina_um.grid(row=0, column=0, sticky='nsew')
        self.pagina_dois.grid(row=0, column=0, sticky='nsew')
        self.mostrar_pagina(self.pagina_um)

        self.dados = {
            'informações':{},
            'atributos':{},
            'atributos_finais':{},
            'características':{},
            'características_finais':{},
            'danos':{},
            'perícias':{},
            'artefatos':{},
            'magias':{}
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

    def mostrar_pagina(self, pagina):
        self.pagina_um.grid_remove()
        self.pagina_dois.grid_remove()
        pagina.grid()

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
                    self.dados = json.load(f)
                
                for secao in self.dados:
                    for k, v in self.dados.get(secao, {}).items():
                        if k in self.dados[secao]:
                            if isinstance(self.dados[secao][k], tk.StringVar):
                                self.dados[secao][k].set(v)

                messagebox.showinfo("Sucesso", "Ficha restaurada!")
            except Exception as e:
                messagebox.showerror('erro', f'Erro ao carregar a ficha :{e}')

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
        
    def criar_combobox(self, text:str, lista_values:list, tamanho_font:int, tamanho_width:int,texto_entrada:str, linha:int, coluna:int):
        ttk.Combobox(
            self, 
            textvariable=text, 
            values=lista_values, 
            font=('Cloister Black Light',tamanho_font), 
            width=tamanho_width
            ).set(texto_entrada).grid(row=linha, column=coluna)
        
    def criar_botao(self,texto:str,comando, cor_fg:str, cor_bg:str, linha:int, coluna:int):
        tk.Button(
            self,
            text=texto, 
            command=comando,
            fg=cor_fg,
            bg=cor_bg
            ).grid(row=linha, column=coluna
        )
 
class PaginaUm(tk.Frame, CriadorDeWidgets):
    def __init__(self, master):
        super().__init__(master, bg='Black')
        self.app_ficha = master
        self.aplicar_pagina_um()

    def dictstr_para_dictint(self, dicionario:dict):
        valores = {}
        for nome, valor in dicionario.items():
            try:
                valores[nome] = float(valor.get())
            except ValueError:
                valores[nome] = 0
        return valores

    def atributo_ativo_para_reativo(self, *args):
        for nome, valor in self.app_ficha.dados['atributos'].items():
            self.app_ficha.dados['atributos_finais'][nome].set(valor.get())

    def calcular_atq_def_vida_sanidade(self, *args):
        valores = self.dictstr_para_dictint(self.app_ficha.dados['atributos_finais'])
        ataque = 2 * ((valores['Força'] + valores['Destreza'] + valores['Inteligência']) / 3)
        defesa = 2 * ((valores['Constituição'] + valores['Agilidade'] + valores['Carisma']) / 3)
        vida = 5 * (valores['Constituição'] + valores['Vitalidade'])
        sanidade = 5 * (valores['Inteligência'] + valores['Carisma'] + valores['Aura'])

        self.app_ficha.dados['características']['Vida'].set(str(vida))
        self.app_ficha.dados['características']['Sanidade'].set(str(sanidade))
        self.app_ficha.dados['características']['Defesa'].set(str(defesa))
        self.app_ficha.dados['características']['Ataque'].set(str(ataque))

    def calcular_dano_vida_sanidade(self, *args):
        valores_int = self.dictstr_para_dictint(self.app_ficha.dados['características'])
        valores_danos_int = self.dictstr_para_dictint(self.app_ficha.dados['danos'])

        vida = valores_int['Vida'] - valores_danos_int['Vida']
        sanidade = valores_int['Sanidade'] - valores_danos_int['Sanidade']
        
        self.app_ficha.dados['características_finais']['Vida'].set(str(vida))
        self.app_ficha.dados['características_finais']['Sanidade'].set(str(sanidade))
        
    def calcular_dano_atributos(self, *args):
        valores_int = self.dictstr_para_dictint(self.app_ficha.dados['atributos'])
        valores_int_car = self.dictstr_para_dictint(self.app_ficha.dados['características'])
        valores_danos_int = self.dictstr_para_dictint(self.app_ficha.dados['danos'])
        
        vitalidade = valores_int['Vitalidade'] - valores_danos_int['Vitalidade']
        mobilidade = valores_int['Mobilidade'] - valores_danos_int['Mobilidade']
        aura = valores_int['Aura'] - valores_danos_int['Aura']
        vida = valores_int_car['Vida'] - valores_danos_int['Vida']
        sanidade = valores_int_car['Sanidade'] - valores_danos_int['Sanidade']
        
        try:
            porcentagem_vit = vitalidade / valores_int['Vitalidade']
            porcentagem_mobi = mobilidade / valores_int['Mobilidade']
            porcentagem_aura = aura / valores_int['Aura']
        except:
            porcentagem_vit = porcentagem_mobi = porcentagem_aura = 1
        
        forca = valores_int['Força'] * porcentagem_vit
        constituicao = valores_int['Constituição'] * porcentagem_vit
        destreza = valores_int['Destreza'] * porcentagem_mobi
        agilidade = valores_int['Agilidade'] * porcentagem_mobi
        inteligencia = valores_int['Inteligência'] * porcentagem_aura
        carisma = valores_int['Carisma'] * porcentagem_aura
        
        self.app_ficha.dados['atributos_finais']['Vitalidade'].set(str(vitalidade))
        self.app_ficha.dados['atributos_finais']['Mobilidade'].set(str(mobilidade))
        self.app_ficha.dados['atributos_finais']['Aura'].set(str(aura))
        self.app_ficha.dados['atributos_finais']['Força'].set(str(forca))
        self.app_ficha.dados['atributos_finais']['Constituição'].set(str(constituicao))
        self.app_ficha.dados['atributos_finais']['Destreza'].set(str(destreza))
        self.app_ficha.dados['atributos_finais']['Agilidade'].set(str(agilidade))
        self.app_ficha.dados['atributos_finais']['Inteligência'].set(str(inteligencia))
        self.app_ficha.dados['atributos_finais']['Carisma'].set(str(carisma))
        self.app_ficha.dados['características_finais']['Vida'].set(str(vida))
        self.app_ficha.dados['características_finais']['Sanidade'].set(str(sanidade))
        
    def criar_campos_informacoes(self, informacao:str, coluna:int):
        self.app_ficha.dados['informação'][informacao] = tk.StringVar(value='')
        if informacao == 'Nome':
            width = 11
        else:
            width = 3
        self.criar_label(
            texto=informacao + ':', 
            tamanho_texto= 11, 
            cor_fg='red', 
            cor_bg='#0C0101',
            linha=1, 
            coluna=coluna,
            tamanho_coluna=1, 
            tipo_sticky='e'
            )
        self.criar_entry(
            str_dict=self.app_ficha.dados['informação'][informacao],
            str_estado='normal', 
            tamanho=width, 
            linha=1, 
            coluna=coluna + 1,
            tipo_sticky='w'
            )
        
    def criar_campo_dano(self, linha:int,atributo:str):
        self.app_ficha.dados['danos'][atributo] = tk.StringVar(value='0')
        self.criar_entry(
            str_dict=self.app_ficha.dados['danos'][atributo],
            str_estado='normal',
            tamanho=3,
            linha=linha,
            coluna=3,
            tipo_sticky='w'
        )
        self.criar_label(
            texto='Dano',
            tamanho_texto=3,
            cor_fg='red',
            cor_bg='#0C0101',
            linha=linha,
            coluna=2,
            tamanho_coluna=1,
            tipo_sticky='e'
        )
        self.app_ficha.dados['danos'][atributo].trace_add('write', self.calcular_dano_atributos)

    def criar_campo_atributo(self, linha:int, atributo:str):
        self.app_ficha.dados['atributos'][atributo] = tk.StringVar(value='0')
        self.app_ficha.dados['atributos_finais'][atributo] = tk.StringVar(value='0')
        self.criar_entry(
            str_dict=self.app_ficha.dados['atributos'][atributo],
            str_estado='normal',
            tamanho=3,
            linha= linha+4,
            coluna=1,
            tipo_sticky='w'
            )
        self.criar_entry(
            str_dict=self.app_ficha.dados['atributos_finais'][atributo],
            str_estado='readonly',
            tamanho=6,
            linha=linha+4,
            coluna=4,
            tipo_sticky='e'
        )
        self.criar_label(
            texto=atributo + ':',
            tamanho_texto=11,
            cor_fg='red',
            cor_bg='#0C0101',
            linha=linha+4,
            coluna=0,
            tamanho_coluna=1,
            tipo_sticky='e'
        )
        if atributo in ['Vitalidade', 'Mobilidade', 'Aura']:
            self.criar_campo_dano(linha+4, atributo)
        self.app_ficha.dados['atributos_finais'][atributo].trace_add('write', self.calcular_atq_def_vida_sanidade)
        self.app_ficha.dados['atributos'][atributo].trace_add('write', self.atributo_ativo_para_reativo)
        
    def criar_campos_caracteristicas(self, caracteristica:str, linha:int):
        self.app_ficha.dados['características'][caracteristica] = tk.StringVar(value='0')
        self.criar_label(
            texto=caracteristica + ':', tamanho_texto=11, 
            cor_fg='red', cor_bg='#0C0101', 
            linha=linha+14, coluna=0, 
            tipo_sticky='e'
        )
        self.criar_entry(
            str_dict=self.app_ficha.dados['características'][caracteristica],
            str_estado='readonly', tamanho=6,
            linha=linha+14, coluna=1,
            tipo_sticky='w'
        )
        if caracteristica in ['Vida', 'Sanidade']:
            self.app_ficha.dados['características_finais'][caracteristica] = tk.StringVar(value='0')
            self.criar_campo_dano(linha+14, caracteristica)
            self.criar_entry(
                str_dict=self.app_ficha.dados['características_finais'][caracteristica],
                str_estado='readonly',
                tamanho=6,
                linha=linha+14,
                coluna=4,
                tipo_sticky='e'
            )

    def criar_campos_pericias(self, pericia:str, linha:int, coluna:int):
        self.dados['perícias'][pericia] = tk.StringVar(value='0')
        self.criar_label(
            texto=pericia + ':', 
            tamanho_texto=11,
            cor_fg='red',
            cor_bg="#0C0101",
            linha=linha+19, 
            coluna=coluna,
            tamanho_coluna=1,
            tipo_sticky='e'
        )
        self.criar_entry(
            str_dict=self.app_ficha.valores_pericias[pericia],
            tamanho=4,
            linha=linha+19,
            coluna=coluna+1,
            tipo_sticky='e'
        )
    def aplicar_pagina_um(self):
        ####################
        #titulo principal posição 0
        ####
        self.criar_label(
            texto='Ficha do personagem.', 
            tamanho_texto= 30,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=0,
            coluna=2,
            tamanho_coluna=4,
            tipo_sticky='e'
        )

        #informaçoes do personagem posiçao 1
        for i, informacao in enumerate(self.app_ficha.informacoes):
            self.criar_campos_informacoes(informacao, i * 2)
            
        #escolha de raça e sexo posição 2
        self.app_ficha.dados['informações']['raça'] = tk.StringVar()
        self.criar_combobox(
            text=self.app_ficha.dados['informações']['raça'],
            lista_values=['Humano', 'Morto-vivo'],
            tamanho_font=11,
            tamanho_width=11,
            texto_entrada='Escolha a raça',
            linha=2,
            coluna=1
        )

        self.app_ficha.dados['informações']['sexo'] = tk.StringVar()
        self.criar_combobox(
            text=self.app_ficha.dados['informações']['sexo'],
            lista_values=['Macho','Fêmea'],
            tamanho_font=11,
            tamanho_width=11,
            texto_entrada='Escolha o sexo',
            linha=2,
            coluna=3
        )

        #titulo dos atributos posiçao 3
        tk.Label(
            root, 
            text='Atributos', 
            font=('Cloister Black Light', 20),
            fg='black',
            bg='#AA0000'
            ).grid(row=3, column=2,columnspan=2)

        #atributos posição 4 a posiçao 12
        for i, atributo in enumerate(self.app_ficha.atributos):
            self.criar_campo_atributo(i, atributo)
            

        #titulo das caracteristicas posição 13
        self.criar_label(
            texto='Características',
            tamanho_texto=20,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=13,
            coluna=2,
            tamanho_coluna=2,
            tipo_sticky='e'
        )

        #caracteristicas posição 14 a 17
        for i, caracteristica in enumerate(self.app_ficha.caracteristicas):
            self.criar_campos_caracteristicas(caracteristica, i)

        #titulo das pericias posiçao 18
        self.criar_label(
            texto='Perícias',
            tamanho_texto=20,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=18,
            coluna=2,
            tamanho_coluna=2,
            tipo_sticky='e'
        )

        #pericias posiçao 19 a 23
        for i, pericia in enumerate(self.app_ficha.pericias):
            linha = i % 4
            coluna = (i // 4) * 2
            self.criar_campos_pericias(pericia, linha, coluna)

        #botoes de salvar e carregar
        self.criar_botao(
            texto='SALVAR',
            comando=self.app_ficha.salvar_dados,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=24,
            coluna=4
        )
        self.criar_botao(
            texto='CARREGAR',
            comando=self.app_ficha.carregar_dados,
            cor_fg='black',
            cor_bg='#AA0000',
            linha=24,
            coluna=5
        )
        self.criar_botao(
            texto='Próxima pagina.',
            comando=lambda: self.app_ficha.mostrar_pagina(self.app_ficha.pagina_dois),
            cor_fg='black',
            cor_bg='#AA0000',
            linha=25,
            coluna=3
        )
        
class PaginaDois(tk.Frame, CriadorDeWidgets):
    def __init__(self, master):
        super().__init__(master, bg='Black')
        self.app_ficha = master
        self.aplicar_pagina_dois()
    
    def aplicar_pagina_dois(self):
        self.criar_botao(
            texto='Página anterior.',
            comando=lambda: self.app_ficha.mostrar_pagina(self.app_ficha.pagina_um),
            cor_fg='black',
            cor_bg='#AA0000',
            linha=25,
            coluna=3
        )

if __name__ == '__main__':
    app = AppFichaDeMortis()
    app.mainloop()