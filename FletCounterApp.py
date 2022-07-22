from cgitb import text
from ctypes import alignment
from turtle import onclick
import flet
from flet import Text,IconButton,icons,Row,Column

def main(page):

    page.title = "Flet Counter"
    page.vertical_alignment = "start"

    t = Text(value="0",text_align="right",width=100,color="green",size=30)

    def minus(e):
        t.value = int(t.value) - 1
        page.update()

    def add(e):
        t.value = int(t.value) + 1
        page.update()

    page.add(
        Column(
            [
                Text(value="\n\nFlet Counter\n",text_align="center",width=1250,color="green",size=30,weight="bold"),
                Row(
                    [
                        IconButton(icons.REMOVE,on_click=minus),
                        t,
                        IconButton(icons.ADD,on_click=add)
                    ],
                    alignment="center"
                )
            ],
        )
    )
flet.app(target = main)