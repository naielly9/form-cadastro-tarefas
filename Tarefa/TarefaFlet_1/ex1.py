#EXERCICIO REALIZADO SEM SER SEPARADO EM CLASS BONITINHO
from typing import Any
import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, pagina: ft.Page, text: str, tipo: str, txt_primeironame: ft.TextField, txt_ultimoname: ft.TextField):
        super().__init__()
        self.text = text
        self.color = ft.colors.BLACK
        self.pagina = pagina  
        self.txt_primeironame = txt_primeironame
        self.txt_ultimoname = txt_ultimoname
        
        if tipo == 'RESETAR':
            self.bgcolor = ft.colors.RED_300
            self.on_click = lambda e: self.btn_reset_clicked()
        elif tipo == 'ENVIAR':
            self.bgcolor = ft.colors.BLUE_300
            self.on_click = lambda e: self.btn_submit_clicked()
        else:
            self.bgcolor = ft.colors.BLUE_300
            self.on_click = lambda e: self.btn_toggle_visibility()

    def btn_toggle_visibility(self):
      self.txt_primeironame.disabled = not self.txt_primeironame.disabled  # Alterna o estado disabled
      self.txt_ultimoname.disabled = not self.txt_ultimoname.disabled  # Alterna o estado disabled
      self.pagina.update()  # Atualiza a página após a alteração  
    
    def btn_reset_clicked(self):
        self.txt_primeironame.value = ""  # Limpa o valor do campo
        self.txt_ultimoname.value = ""  # Limpa o valor do campo
        self.txt_primeironame.label = "Primeiro nome"  # Redefine o label
        self.txt_ultimoname.label = "Último nome"  # Redefine o label
        self.txt_primeironame.error_text = None  # Limpa o texto de erro
        self.txt_ultimoname.error_text = None  # Limpa o texto de erro
        self.pagina.update()  # Atualiza a página após a redefinição
    
    def btn_submit_clicked(self):
        if not self.txt_primeironame.value:
            self.txt_primeironame.error_text = "Por favor, digite seu primeiro nome."
            self.pagina.update()  
            return 
        
        primeiro_name = self.txt_primeironame.value
        self.txt_primeironame.error_text = None
        self.txt_primeironame.label = "Formulário enviado!"
        self.txt_primeironame.value = "Formulário enviado!"
        
        if not self.txt_ultimoname.value:
            self.txt_ultimoname.error_text = "Por favor, digite seu último nome."
            self.pagina.update()  
            return  
        
        ultimo_name = self.txt_ultimoname.value
        self.txt_ultimoname.label = "Formulário enviado!"
        self.txt_ultimoname.value = "Formulário enviado!"
        self.txt_ultimoname.error_text = None
        self.pagina.update()  

def main(pagina: ft.Page):
    # Defina o tema da página
    pagina.title = "Cadastro"
    pagina.theme = ft.Theme(
        primary_color=ft.colors.BLUE_500,
        font_family="Arial"
    )

    # Cabeçalho 
    header = ft.Container(
        content=ft.Text("Formulário de Cadastro", size=30, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        padding=20,
        alignment=ft.alignment.center
    )

    # Campos de entrada
    txt_primeironame = ft.TextField(
        label="Primeiro nome",
    )
    txt_ultimoname = ft.TextField(
        label="Último nome",
    )

    # Botões
    reset_clicked = MyButton(pagina, text="RESETAR", tipo="RESETAR", txt_primeironame=txt_primeironame, txt_ultimoname=txt_ultimoname)
    submit_clicked = MyButton(pagina, text="ENVIAR", tipo="ENVIAR", txt_primeironame=txt_primeironame, txt_ultimoname=txt_ultimoname)
    toggle_visibility = MyButton(pagina, text="ALTERAR VISIBILIDADE", tipo="ALTERAR VISIBILIDADE", txt_primeironame=txt_primeironame, txt_ultimoname=txt_ultimoname)

    # Layout principal
    pagina.add(
        header,
        ft.Container(
            content=ft.Column(
                [
                    txt_primeironame,
                    txt_ultimoname,
                    ft.Row(
                        [reset_clicked, submit_clicked, toggle_visibility],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,  
            alignment=ft.alignment.center,  # Alinhamento centralizado
            border_radius=10,
            bgcolor=ft.colors.GREY_200,  # Cor de fundo cinza
            width="100%",  # Largura total para responsividade
        ),
    )

ft.app(target=main, view=ft.WEB_BROWSER)
