import flet
from flet import Page,Row,TextField,ElevatedButton,Text
from time import sleep

def main(page: Page):

    # Event Handling

    def btn_clicked(e):
        page.add(Text("sweet name!"))

    for i in range(10):
        page.controls.append(Text(f"Line{i}"))
        if i > 4 :
            page.controls.pop()
        page.update()
        sleep(0.3)
    
    page.add(
        Row(
            controls=[
                TextField(label="Your name"),
                ElevatedButton(text="Say my name!",on_click=btn_clicked)
            ]
        )
    )
    


flet.app(target=main)

