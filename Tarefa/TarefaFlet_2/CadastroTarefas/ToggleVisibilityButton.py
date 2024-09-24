import flet as ft
from .MyButton import myButton

class toggleVisibilityButton(myButton):
    def __init__(self, pagina: ft.Page, text: str, txt_tarefa: ft.TextField, task_list: list, task_column: ft.Column):
        super().__init__(pagina, text, txt_tarefa, task_list, task_column)
        self.bgcolor = ft.colors.BLUE_300
        self.on_click = self.btn_toggle_visibility

    def btn_toggle_visibility(self, e):
        self.task_column.visible = not self.task_column.visible
        self.txt_tarefa.disabled = not self.txt_tarefa.disabled
        if self.txt_tarefa.disabled:
            self.txt_tarefa.label = ""
        else:
            self.txt_tarefa.label = "Adicionar tarefas"
        self.pagina.update()