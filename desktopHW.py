import flet
from flet import Page,Text

def main(page: Page):
    txt = Text(value="Hello World!!!!! \n It's me Hilfa here :)",color="green")
    page.controls.append(txt)
    page.update()

flet.app(target=main,view=flet.WEB_BROWSER)