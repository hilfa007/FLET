import flet
from flet import*

def main(page):
    # ToDo
    def add_click(e):
        page.add(Checkbox(label=new_task.value))

    new_task = TextField(hint_text="whats need to be done?",width=300)
    page.add(
        Row(
            [new_task,
            ElevatedButton("Add",on_click=add_click)]
        )
    )


flet.app(target=main)