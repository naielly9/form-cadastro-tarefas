import flet as ft
from .MyButton import myButton

class clear(myButton):
    def __init__(self, pagina: ft.Page, text: str, txt_tarefa: ft.TextField, task_list: list, task_column: ft.Column):
        super().__init__(pagina, text, txt_tarefa, task_list, task_column)
        self.bgcolor = ft.colors.RED_300
        self.on_click = self.btn_clear_list

    def btn_clear_list(self, e):
        self.txt_tarefa.value = ""
        self.txt_tarefa.label = "Adicionar tarefas"
        self.txt_tarefa.error_text = None
        self.task_list.clear()
        self.update_task_list()

    def update_task_list(self):
        self.task_column.controls.clear()
        self.pagina.update()
