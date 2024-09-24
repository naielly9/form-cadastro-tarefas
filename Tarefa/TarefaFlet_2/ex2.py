#EXERCICIO REALIZADO SEM SER SEPARADO EM CLASS BONITINHO
import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, pagina: ft.Page, text: str, tipo: str, txt_tarefa: ft.TextField, task_list: list, task_column: ft.Column):
        super().__init__()
        self.text = text
        self.color = ft.colors.BLACK
        self.pagina = pagina  
        self.txt_tarefa = txt_tarefa
        self.task_list = task_list
        self.task_column = task_column
        
        if tipo == 'RESETAR':
            self.bgcolor = ft.colors.RED_300
            self.on_click = lambda e: self.btn_clear_list()
        elif tipo == 'ENVIAR':
            self.bgcolor = ft.colors.BLUE_300
            self.on_click = lambda e: self.btn_add_task()
        else:
            self.bgcolor = ft.colors.BLUE_300
            self.on_click = lambda e: self.btn_toggle_visibility()

    def btn_toggle_visibility(self):
        self.task_column.visible = not self.task_column.visible
        self.txt_tarefa.disabled = not self.txt_tarefa.disabled
        if self.txt_tarefa.disabled:
            self.txt_tarefa.label = ""
        else:
            self.txt_tarefa.label = "Adicionar tarefas"
        self.pagina.update() 
    
    def btn_clear_list(self):
        print("Botão Resetar clicado")
        self.txt_tarefa.value = ""
        self.txt_tarefa.label = "Adicionar tarefas"   
        self.txt_tarefa.error_text = None
        self.task_list.clear()
        self.update_task_list()
        self.pagina.update()  
    
    def btn_add_task(self):
        print("Botão Enviar clicado")
        if not self.txt_tarefa.value:
            self.txt_tarefa.error_text = "Por favor, digite a tarefa."
            self.pagina.update()  
            return 
        
        tarefa_name = self.txt_tarefa.value
        self.txt_tarefa.error_text = None
        self.txt_tarefa.value = ""
        self.task_list.append(tarefa_name)
        self.update_task_list()
        self.pagina.update()
    
    def update_task_list(self):
        print("Atualizando lista de tarefas")
        self.task_column.controls.clear()
        for task in self.task_list:
            print(f"Adicionando tarefa: {task}")
            self.task_column.controls.append(ft.ListTile(
                leading=ft.Icon(ft.icons.CIRCLE),
                title=ft.Text(task),
            ))
        self.pagina.update()

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
    reset_clicked = MyButton(pagina, text="RESETAR", tipo="RESETAR", txt_tarefa=txt_tarefa, task_list=task_list, task_column=task_column)
    submit_clicked = MyButton(pagina, text="ENVIAR", tipo="ENVIAR", txt_tarefa=txt_tarefa, task_list=task_list, task_column=task_column)
    toggle_visibility = MyButton(pagina, text="ALTERAR VISIBILIDADE", tipo="ALTERAR VISIBILIDADE", txt_tarefa=txt_tarefa, task_list=task_list, task_column=task_column)

    # Layout principal
    pagina.add(
        header,
        ft.Container(
            content=ft.Column(
                [
                    txt_tarefa,
                    ft.Row(
                        [reset_clicked, submit_clicked, toggle_visibility],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    task_column,
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
