import flet
from flet import*

def main(page):
    
    # Text Styles
    t = Text(
        value ="Hi! Hilfa Here.. How Are You All?" ,
        color ="white",size = 45,
        bgcolor ="cyan",
        italic = True,weight ="bold"
    )
    page.add(t)


flet.app(target=main)