import tkinter as tk
from tkinter import PhotoImage
import sys
from io import StringIO

def chamar_menu(param):
    output = sys.stdout 
    sys.stdout = StringIO()
    match param:
        case 0:
            print("EEeeEeE ueUuuuUUuuuuUU SssSOOoooOuuuuUU O CaaAVeeeiRAaaa")
        case 1:
            print("eu chou u caveirinha")
        case 2:
            print("eu cav")
        case 3:
            print("CRANIUUUUUUUM PRESENTE")
        case 4:
            print("Saudações a todos, sou o senhor caveira!")
        case 5:
            print("im a skul man")
    terminal_text.config(state=tk.NORMAL)
    terminal_text.insert(tk.END, sys.stdout.getvalue())
    terminal_text.config(state=tk.DISABLED)

    # Redireciona a saída de volta ao padrão
    sys.stdout = output
def button_click(index):
    #print(f"Botão {index + 1} clicado!")
    chamar_menu(index)
#########################################################
############### MUDA AQUI O DIRETORIO ###################
#########################################################
##########\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#########
diretorio='C:\\Users\\Zhafyr\\Desktop\\codegos\\caveiras'
root = tk.Tk()
root.title("Menu com Imagens")
background_image = PhotoImage(file=f"{diretorio}\\fundo.png")  
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
button_data = [
    {"image": f"{diretorio}\\botao1.png", "text": "CaaAVeeeiRAaaa"},  
    {"image": f"{diretorio}\\botao2.png", "text": "caveirinha"},  
    {"image": f"{diretorio}\\botao3.png", "text": "cav"},  
    {"image": f"{diretorio}\\botao4.png", "text": "CRANIUM"}, 
    {"image": f"{diretorio}\\botao5.png", "text": "Sr. Caveira"},  
    {"image": f"{diretorio}\\botao6.png", "text": "skul"},  
]
mid = len(button_data) // 2 
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=20)

right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=20)

for index, data in enumerate(button_data):
    img = PhotoImage(file=data["image"])
    button = tk.Button(left_frame if index < mid else right_frame, image=img, text=data["text"], compound="top", command=lambda index=index: button_click(index))
    button.pack(pady=10)
    button.image = img

terminal_frame = tk.Frame(root)
terminal_frame.pack(fill="both", expand=True)
terminal_frame.place(relx=0.15, rely=0.6, relwidth=0.7, relheight=0.35)
terminal_text = tk.Text(terminal_frame, wrap=tk.WORD)
terminal_text.pack(fill="both", expand=True)
terminal_text.config(state=tk.DISABLED)
root.state("zoomed") 
root.mainloop()