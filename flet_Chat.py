import flet
from flet import Page,Row,Column,ElevatedButton,Text,TextField

def main(page):
    
    def on_message(msg):
        messages.controls.append(Text(msg))
        page.update()
    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f" {user.value} : {message.value} ")
        message.value = ""
        page.update()

    messages = Column()
    user = TextField(hint_text = "your name",width = 150)
    message = TextField(hint_text = "your message",expand = True)
    send = ElevatedButton("send",on_click=send_click)
    page.add(messages,Row(controls=[user,message,send]))
    page.update()
    
flet.app(target=main)


