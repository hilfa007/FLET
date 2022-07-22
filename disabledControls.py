import flet
from flet import*

def main(page):
    
    f_name = TextField()
    l_name = TextField()
    f_name.disabled = True
    l_name.disabled = True
    page.add(f_name,l_name)

    # Or
    email = TextField()
    btn = ElevatedButton()
    c = Column(controls=[
        email,
        btn
    ])
    c.disabled = True
    page.add(c)

flet.app(target=main)
