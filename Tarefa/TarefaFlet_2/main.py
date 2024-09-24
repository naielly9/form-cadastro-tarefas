import flet as ft
from CadastroTarefas import myButton, add, clear, toggleVisibilityButton

def main(pagina: ft.Page):
    # Defina o tema da página
    pagina.title = "Tarefas"
    pagina.theme = ft.Theme(
        primary_color=ft.colors.BLUE_500,
        font_family="Arial"
    )

    # Cabeçalho 
    header = ft.Container(
        content=ft.Text("Lista de Tarefas", size=30, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE,
        padding=20,
        alignment=ft.alignment.center
    )

    # Campos de entrada
    txt_tarefa = ft.TextField(
        label="Adicionar tarefas",
    )

    # Lista de tarefas e coluna para exibir as tarefas
    task_list = []
    task_column = ft.Column()

    # Botões
    reset_button = clear(pagina, text="RESETAR", txt_tarefa=txt_tarefa, task_list=task_list, task_column=task_column)
    submit_button = add(pagina, text="ENVIAR", txt_tarefa=txt_tarefa, task_list=task_list, task_column=task_column)
    toggle_visibility_button = toggleVisibilityButton(pagina, text="ALTERAR VISIBILIDADE", txt_tarefa=txt_tarefa, task_list=task_list, task_column=task_column)

    # Layout principal
    pagina.add(
        header,
        ft.Container(
            content=ft.Column(
                [
                    txt_tarefa,
                    ft.Row(
                        [reset_button, submit_button, toggle_visibility_button],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    task_column,
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            alignment=ft.alignment.center,  
            border_radius=10,
            bgcolor=ft.colors.GREY_200, 
            width="100%",  
        ),
    )

ft.app(target=main, view=ft.WEB_BROWSER)
