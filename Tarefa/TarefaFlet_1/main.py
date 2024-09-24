import flet as ft
from Cadastro import myButton, clear, add, toggleVisibilityButton

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
    reset_button = clear(pagina, text="RESETAR", txt_primeironame=txt_primeironame, txt_ultimoname=txt_ultimoname)
    submit_button = add(pagina, text="ENVIAR", txt_primeironame=txt_primeironame, txt_ultimoname=txt_ultimoname)
    toggle_visibility_button = toggleVisibilityButton(pagina, text="ALTERAR VISIBILIDADE", txt_primeironame=txt_primeironame, txt_ultimoname=txt_ultimoname)

    # Layout principal
    pagina.add(
        header,
        ft.Container(
            content=ft.Column(
                [
                    txt_primeironame,
                    txt_ultimoname,
                    ft.Row(
                        [reset_button, submit_button, toggle_visibility_button],
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