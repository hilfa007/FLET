import flet
from flet import Page,Text

def main(page: Page):
    for i in range(2000):
        page.controls.append(Text(f"Line {i}"))
    page.scroll = "always"
    page.update() 

flet.app(target=main, view=flet.WEB_BROWSER)