import flet
from flet import Page,Text,ListView

def main(page: Page):
    lv = ListView(expand=True, spacing=10)
    for i in range(2000):
        lv.controls.append(Text(f"Line {i}"))
    page.add(lv)

flet.app(target=main)