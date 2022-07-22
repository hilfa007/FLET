import flet
from flet import Page,Text

def main(page: Page):
    # Let's Say Hello To Flet :)
    txt = Text(value="Hello World!!!!! \n It's me Hilfa here :)",color="green")
    page.controls.append(txt)
    page.update()

flet.app(target=main)