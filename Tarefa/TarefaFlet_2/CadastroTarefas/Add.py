import flet as ft
from .MyButton import myButton

class add(myButton):
    def __init__(self, pagina: ft.Page, text: str, txt_tarefa: ft.TextField, task_list: list, task_column: ft.Column):
        super().__init__(pagina, text, txt_tarefa, task_list, task_column)
        self.bgcolor = ft.colors.BLUE_300
        self.on_click = self.btn_add_task

    def btn_add_task(self, e):
        if not self.txt_tarefa.value:
            self.txt_tarefa.error_text = "Por favor, digite a tarefa."
            self.pagina.update()
            return

        tarefa_name = self.txt_tarefa.value
        self.txt_tarefa.error_text = None
        self.txt_tarefa.value = ""
        self.task_list.append(tarefa_name)
        self.update_task_list()

    def update_task_list(self):
        self.task_column.controls.clear()
        for task in self.task_list:
            self.task_column.controls.append(ft.ListTile(
                leading=ft.Icon(ft.icons.CIRCLE),
                title=ft.Text(task),
            ))
        self.pagina.update()