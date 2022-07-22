import os,flet
from flet import Container, Page, GridView, Text, alignment, border, border_radius, colors
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
def main(page: Page):
    gv = GridView(expand=True, max_extent=100, child_aspect_ratio=1)
    page.add(gv)

    for i in range(100):
        gv.controls.append(
            Container(
                Text(f"Product {i}"),
                alignment=alignment.center,
                bgcolor=colors.BLACK26,
                border=border.all(1, colors.BLACK26),
                border_radius=border_radius.all(5),
            )
        )
    page.update()
flet.app(target=main)