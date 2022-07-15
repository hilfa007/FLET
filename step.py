import flet
from flet import Page,Text,Row
from time import sleep

def main(page: Page):
    page.add(
        Row(
            controls = [
                Text("A",color="green"),
                Text("B",color="blue"),
                Text("C",color="red")
            ]

        )
    )
    t = Text(color="blue")
    page.add(t)
    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        sleep(1)
    
flet.app(target=main)