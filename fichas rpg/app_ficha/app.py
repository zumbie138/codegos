import tkinter as tk
from dados import DadosFicha
from pagina_um import PaginaUm
from pagina_dois import PaginaDois

class AppFichaDeMortis(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ficha de RPG De Mortis')
        self.configure(bg='Black')
        self.dados_ficha = DadosFicha()
        self.pagina_um = PaginaUm(self, self.dados_ficha)
        self.pagina_dois = PaginaDois(self, self.dados_ficha)
        self.pagina_um.grid(row=0, column=0, sticky='nsew')
        self.pagina_dois.grid(row=0, column=0, sticky='nsew')
        self.mostrar_pagina(self.pagina_um)

    def mostrar_pagina(self, pagina):
        self.pagina_um.grid_remove()
        self.pagina_dois.grid_remove()
        pagina.grid()



if __name__ == '__main__':
    app = AppFichaDeMortis()
    app.mainloop()