import flet as ft

class myButton(ft.ElevatedButton):
    def __init__(self, pagina: ft.Page, text: str, txt_primeironame: ft.TextField, txt_ultimoname: ft.TextField):
        super().__init__()
        self.text = text
        self.color = ft.colors.BLACK
        self.pagina = pagina
        self.txt_primeironame = txt_primeironame
        self.txt_ultimoname = txt_ultimoname
