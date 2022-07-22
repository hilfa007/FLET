import flet
from flet import Container, Draggable, DragTarget, Page, Row, Text, alignment, colors ,border

def main(page: Page):

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.data)
        # update text inside draggable control
        src.content.content.value = "item dragged"
        # update text inside drag target control
        e.control.content.content.value = "item dropped"
        e.control.content.border = None
        page.update()

    def drag_will_accept(e):
        # black border when it's allowed to drop and red when it's not
        e.control.content.border = border.all(
            2, colors.BLACK45 if e.data == "true" else colors.RED
        )
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        Row(
            [
                Draggable(
                    group="number",
                    content=Container(
                        width=100,
                        height=100,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("1", size=10),
                        alignment=alignment.center,
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=Text("1"),
                ),
                Draggable(
                    group="number",
                    content=Container(
                        width=100,
                        height=100,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("2", size=10),
                        alignment=alignment.center,
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=Text("2"),
                ),
            
                DragTarget(
                    group="number",
                    content=Container(
                        width=100,
                        height=100,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text("0", size=10),
                        alignment=alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )

flet.app(target=main)