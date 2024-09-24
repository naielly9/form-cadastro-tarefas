import flet as ft
from .MyButton import myButton

class add(myButton):
    def __init__(self, pagina: ft.Page, text: str, txt_primeironame: ft.TextField, txt_ultimoname: ft.TextField):
        super().__init__(pagina, text, txt_primeironame, txt_ultimoname)
        self.bgcolor = ft.colors.BLUE_300
        self.on_click = self.btn_submit_clicked

    def btn_submit_clicked(self, e):
        if not self.txt_primeironame.value:
            self.txt_primeironame.error_text = "Por favor, digite seu primeiro nome."
            self.pagina.update()
            return

        primeiro_name = self.txt_primeironame.value
        self.txt_primeironame.error_text = None
        self.txt_primeironame.value = "Formulário enviado!"

        if not self.txt_ultimoname.value:
            self.txt_ultimoname.error_text = "Por favor, digite seu último nome."
            self.pagina.update()
            return

        ultimo_name = self.txt_ultimoname.value
        self.txt_ultimoname.value = "Formulário enviado!"
        self.txt_ultimoname.error_text = None
        self.pagina.update()
