import flet as ft
from .MyButton import myButton

class clear(myButton):
    def __init__(self, pagina: ft.Page, text: str, txt_primeironame: ft.TextField, txt_ultimoname: ft.TextField):
        super().__init__(pagina, text, txt_primeironame, txt_ultimoname)
        self.bgcolor = ft.colors.RED_300
        self.on_click = self.btn_reset_clicked

    def btn_reset_clicked(self, e):
        self.txt_primeironame.value = ""
        self.txt_ultimoname.value = ""
        self.txt_primeironame.label = "Primeiro nome"
        self.txt_ultimoname.label = "Último nome"
        self.txt_primeironame.error_text = None
        self.txt_ultimoname.error_text = None
        self.pagina.update()
