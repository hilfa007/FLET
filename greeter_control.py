import flet
import threading,time
from flet import Page,UserControl,Text,Column,TextField,ElevatedButton,Row

class GreeterControl(UserControl):
    def build(self):
        return Row([
            TextField(label="your name"),
            ElevatedButton("login")
        ])
class CountDown(UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = Text()
        return self.countdown

class Counter(UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count

    def build(self):
        text = Text(str(self.counter))
        def add(e):
            self.counter += 1
            text.value = str(self.counter)
            self.update()
        return Row([text, ElevatedButton("Add", on_click=add)])

def main(page):
    page.add(Counter(100),Column(),GreeterControl(),Column(),Counter(200),CountDown(100))


flet.app(target=main)