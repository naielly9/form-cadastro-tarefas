import flet as ft
from .MyButton import myButton

class toggleVisibilityButton(myButton):
    def __init__(self, pagina: ft.Page, text: str, txt_primeironame: ft.TextField, txt_ultimoname: ft.TextField):
        super().__init__(pagina, text, txt_primeironame, txt_ultimoname)
        self.bgcolor = ft.colors.BLUE_300
        self.on_click = self.btn_toggle_visibility

    def btn_toggle_visibility(self, e):
        self.txt_primeironame.disabled = not self.txt_primeironame.disabled
        self.txt_ultimoname.disabled = not self.txt_ultimoname.disabled
        if self.txt_primeironame.disabled and self.txt_ultimoname.disabled:
            self.txt_primeironame.label = ""
            self.txt_ultimoname.label = ""
        else:
            self.txt_primeironame.label = "Primeiro nome"
            self.txt_ultimoname.label = "Último nome"
        self.pagina.update()