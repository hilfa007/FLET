from typing import Text
import flet
from flet import ElevatedButton,TextField,Text

def main(page):
    def btn_click(e):
        if not txt.value:
            txt.error_text = "Please Enter Your Name"
            page.update()
        else:
            name = txt.value
            page.clean()
            page.add(Text(f"Hello, {name}!..",color="blue",size=30,weight="bold"))

    txt = TextField(label="your name")
    page.add(txt,ElevatedButton("Say Hello",on_click=btn_click))


flet.app(target=main)