import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import json

root = tk.Tk()
root.configure(bg='Black')
root.title('Ficha de RPG De Mortis')

valores_infos = {}
valores_atr = {}
valores_atr_final = {}
valores_car = {}
valores_car_final = {}
valores_danos = {}
valores_pericias = {}


informacoes = ['Nome', 'Level', 'Idade', 'Altura']
caracteristicas = ['Ataque', 'Defesa', 'Vida', 'Sanidade']
atributos = ['Força', 'Constituição','Vitalidade',
             'Destreza','Agilidade','Mobilidade',
             'Inteligência','Carisma','Aura']
pericias = ['Arte marcial', 'Perícia com armas','Atletismo',
            'Saúde','Acrobacia','Malandragem',
            'Furtividade','Equilibrio','Habilidades artísticas',
            'Blefar','Medicina','Conhecimento']

def criar_entry(str_dict:str, str_estado:str,tamanho:int,linha:int,coluna:int):
    tk.Entry(
        root, 
        textvariable=str_dict, 
        state=str_estado, 
        width=tamanho).grid(row=linha,column=coluna)
    
def criar_label(texto:str, tamanho_texto:int, cor_fg:str, cor_bg:str, linha:int, coluna:int, tamanho_coluna:int, tipo_sticky:str):
    tk.Label(
    root, 
    text=texto, 
    font=('Cloister Black Light', tamanho_texto),
    fg=cor_fg,
    bg=cor_bg
    ).grid(
        row=linha, 
        column=coluna, 
        columnspan=tamanho_coluna,
        sticky=tipo_sticky)
    
def dictstr_para_dictint(dicionario:dict):
    valores = {}
    for nome, valor in dicionario.items():
        try:
            valores[nome] = float(valor.get())
        except ValueError:
            valores[nome] = 0
    return valores

def atributo_ativo_para_reativo(*args):
    for nome, valor in valores_atr.items():
        valores_atr_final[nome].set(valor.get())
    
def calcular_atq_def_vida_sanidade(*args):
    valores = dictstr_para_dictint(valores_atr_final)
    ataque = 2 * ((valores['Força'] + valores['Destreza'] + valores['Inteligência']) / 3)
    defesa = 2 * ((valores['Constituição'] + valores['Agilidade'] + valores['Carisma']) / 3)
    vida = 5 * (valores['Constituição'] + valores['Vitalidade'])
    sanidade = 5 * (valores['Inteligência'] + valores['Carisma'] + valores['Aura'])
    
    valores_car['Vida'].set(str(vida))
    valores_car['Sanidade'].set(str(sanidade))
    valores_car['Defesa'].set(str(defesa))
    valores_car['Ataque'].set(str(ataque))

def calcular_dano_vida_sanidade(*args):
    valores_int = dictstr_para_dictint(valores_car)
    valores_danos_int = dictstr_para_dictint(valores_danos)
    
    vida = valores_int['Vida'] - valores_danos_int['Vida']
    sanidade = valores_int['Sanidade'] - valores_danos_int['Sanidade']
    
    valores_car_final['Vida'].set(str(vida))
    valores_car_final['Sanidade'].set(str(sanidade))
    
def calcular_dano_atributos(*args):
    valores_int = dictstr_para_dictint(valores_atr)
    valores_int_car = dictstr_para_dictint(valores_car)
    valores_danos_int = dictstr_para_dictint(valores_danos)
    
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
    
    valores_atr_final['Vitalidade'].set(str(vitalidade))
    valores_atr_final['Mobilidade'].set(str(mobilidade))
    valores_atr_final['Aura'].set(str(aura))
    valores_atr_final['Força'].set(str(forca))
    valores_atr_final['Constituição'].set(str(constituicao))
    valores_atr_final['Destreza'].set(str(destreza))
    valores_atr_final['Agilidade'].set(str(agilidade))
    valores_atr_final['Inteligência'].set(str(inteligencia))
    valores_atr_final['Carisma'].set(str(carisma))
    valores_car_final['Vida'].set(str(vida))
    valores_car_final['Sanidade'].set(str(sanidade))
    
def criar_campos_informacoes(informacao:str, coluna:int):
    valores_infos[informacao] = tk.StringVar(value='')
    if informacao == 'Nome':
        width = 11
    else:
        width = 3
    tk.Label(root, text=informacao + ':', font=('Cloister Black Light', 11), fg='red', bg='#0C0101').grid(row=1, column=coluna, sticky='e')
    tk.Entry(root, textvariable=valores_infos[informacao], width=width).grid(row=1, column=coluna + 1, sticky='w') 
    
def criar_campo_dano(linha:int,atributo:str):
    valores_danos[atributo] = tk.StringVar(value='0')
    tk.Entry(root, textvariable=valores_danos[atributo], width=3).grid(row=linha,column=3,sticky='w')
    tk.Label(root, text='Dano:',font=('Cloister Black Light',9),fg='red',bg="#0C0101").grid(row=linha, column=2,sticky='e')
    valores_danos[atributo].trace_add('write', calcular_dano_atributos)

def criar_campo_atributo(linha:int, atributo:str):
    valores_atr[atributo] = tk.StringVar(value='0')
    valores_atr_final[atributo] = tk.StringVar(value='0')
    entry_ativo = tk.Entry(root, textvariable=valores_atr[atributo], width=3)
    entry_reativo = tk.Entry(root, textvariable=valores_atr_final[atributo], state='readonly', width=6)
    label = tk.Label(root, text=atributo + ':', font=('Cloister Black Light',11),fg='red',bg="#0C0101")
    label.grid(row=linha+4, column=0, sticky='e')
    entry_ativo.grid(row=linha+4, column=1, sticky='w')
    entry_reativo.grid(row=linha+4, column=4, sticky='e')
    if atributo in ['Vitalidade', 'Mobilidade', 'Aura']:
        criar_campo_dano(linha+4, atributo)
    valores_atr_final[atributo].trace_add('write', calcular_atq_def_vida_sanidade)
    valores_atr[atributo].trace_add('write', atributo_ativo_para_reativo)
    
def criar_campos_caracteristicas(caracteristica:str, linha:int):
    valores_car[caracteristica] = tk.StringVar(value='0')
    tk.Label(root, text=caracteristica + ':', font=('Cloister Black Light',11),fg='red',bg="#0C0101").grid(row=linha+14, column=0, sticky='e')
    tk.Entry(root, textvariable=valores_car[caracteristica], state='readonly', width=6).grid(row=linha+14, column=1,sticky='w')
    if caracteristica in ['Vida', 'Sanidade']:
        valores_car_final[caracteristica] = tk.StringVar(value='0')
        criar_campo_dano(linha+14, caracteristica)
        tk.Entry(root, textvariable=valores_car_final[caracteristica], state='readonly',width=6).grid(row=linha+14,column=4)

def criar_campos_pericias(pericia:str, linha:int, coluna:int):
    valores_pericias[pericia] = tk.StringVar(value='0')
    tk.Label(root, text=pericia + ':', font=('Cloister Black Light',11),fg='red',bg="#0C0101").grid(row=linha+19, column=coluna)
    tk.Entry(root, textvariable=valores_pericias[pericia],width=4).grid(row=linha+19,column=coluna+1)

def salvar_dados():
    dados ={
        "infos": {k: v.get() for k, v in valores_infos.items()},
        "atributos": {k: v.get() for k, v in valores_atr.items()},
        "atributos_finais": {k: v.get() for k, v in valores_atr_final.items()},
        "caracteristicas": {k: v.get() for k, v in valores_car.items()},
        "caracteristicas_finais": {k: v.get() for k, v in valores_car_final.items()},
        "danos": {k: v.get() for k, v in valores_danos.items()},
        "pericias": {k: v.get() for k, v in valores_pericias.items()},
    }
    caminho = filedialog.asksaveasfilename(
        defaultextension='.json',
        filetypes=[('Arquivos JSON','*.json')],
        title='Salvar ficha.'
    )
    if caminho:
        try:
            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
                messagebox.showinfo('Sucesso','Sucesso, a ficha foi salva!')
        except Exception as e:
            messagebox.showerror('erro', f'erro ao salvar: {e}')

def carregar_dados():
    caminho = filedialog.askopenfilename(
        defaultextension='.json',
        filetypes=[('Arquivos JSON','*.json')],
        title='Carregar ficha.'
    )
    if caminho:
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                
            for k, v in dados.get("infos", {}).items():
                if k in valores_infos:
                    valores_infos[k].set(v)

            for k, v in dados.get("atributos", {}).items():
                if k in valores_atr:
                    valores_atr[k].set(v)

            for k, v in dados.get("atributos_finais", {}).items():
                if k in valores_atr_final:
                    valores_atr_final[k].set(v)

            for k, v in dados.get("caracteristicas", {}).items():
                if k in valores_car:
                    valores_car[k].set(v)

            for k, v in dados.get("caracteristicas_finais", {}).items():
                if k in valores_car_final:
                    valores_car_final[k].set(v)

            for k, v in dados.get("danos", {}).items():
                if k in valores_danos:
                    valores_danos[k].set(v)

            for k, v in dados.get("pericias", {}).items():
                if k in valores_pericias:
                    valores_pericias[k].set(v)

            messagebox.showinfo("Sucesso", "Ficha restaurada!")
        except Exception as e:
            messagebox.showerror('erro', f'Erro ao carregar a ficha :{e}')
####################
#titulo principal posição 0
####
tk.Label(
    root, 
    text='Ficha do personagem.', 
    font=('Cloister Black Light', 30),
    fg='black',
    bg='#AA0000'
    ).grid(row=0, column=2,columnspan=4)

#informaçoes do personagem posiçao 1
for i, informacao in enumerate(informacoes):
    criar_campos_informacoes(informacao, i * 2)
    
#escolha de raça e sexo posição 2
raca = tk.StringVar()
combo_raca = ttk.Combobox(root, textvariable=raca, values=['Humano','Morto-vivo'], font=('Cloister Black Light',11), width=11)
combo_raca.set('Escolha a raça')
combo_raca.grid(row=2, column=1)
sexo = tk.StringVar()
combo_sexo = ttk.Combobox(root, textvariable=sexo, values=['Macho','Fêmea'], font=('Cloister Black Light',11), width=11)
combo_sexo.set('Escolha o sexo')
combo_sexo.grid(row=2, column=3)

#titulo dos atributos posiçao 3
tk.Label(
    root, 
    text='Atributos', 
    font=('Cloister Black Light', 20),
    fg='black',
    bg='#AA0000'
    ).grid(row=3, column=2,columnspan=2)

#atributos posição 4 a posiçao 12
for i, atributo in enumerate(atributos):
    criar_campo_atributo(i, atributo)
    

#titulo das caracteristicas posição 13
tk.Label(
    root, 
    text='Características', 
    font=('Cloister Black Light', 20),
    fg='black',
    bg='#AA0000'
    ).grid(row=13, column=2,columnspan=2)

#caracteristicas posição 14 a 17
for i, caracteristica in enumerate(caracteristicas):
    criar_campos_caracteristicas(caracteristica, i)

#titulo das pericias posiçao 18
tk.Label(
    root, 
    text='Perícias', 
    font=('Cloister Black Light', 20),
    fg='black',
    bg='#AA0000'
    ).grid(row=18, column=2,columnspan=2)

#pericias posiçao 19 a 23
for i, pericia in enumerate(pericias):
    linha = i % 4
    coluna = (i // 4) * 2
    criar_campos_pericias(pericia, linha, coluna)

#botoes de salvar e carregar
tk.Button(root, text='SALVAR', command=salvar_dados, fg='black',bg='#AA0000').grid(row=24, column=4)
tk.Button(root, text='CARREGAR', command=carregar_dados, fg='black',bg='#AA0000').grid(row=24, column=5)
    
root.mainloop()