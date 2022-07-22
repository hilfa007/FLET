import flet
from flet import ListView, Page, Text

def main(page: Page):

    # add ListView to a page first
    lv = ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(Text(f"Line {i}"))
        # send page to a page
        if i % 500 == 0:
            page.update()
    # send the rest to a page
    page.update()

flet.app(target=main)