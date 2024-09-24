import flet as ft

class myButton(ft.ElevatedButton):
     def __init__(self, pagina: ft.Page, text: str, txt_tarefa: ft.TextField, task_list: list, task_column: ft.Column):
        super().__init__()
        self.text = text
        self.color = ft.colors.BLACK
        self.pagina = pagina
        self.txt_tarefa = txt_tarefa
        self.task_list = task_list
        self.task_column = task_column
