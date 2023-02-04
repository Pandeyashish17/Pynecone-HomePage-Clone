
from .navbar import navbar

import pynecone as pc

class State(pc.State):
    pass


def index():
    return pc.center(
        pc.vstack(
            navbar(),
            pc.heading("Frontend",font_size="4em" ),
            pc.heading("Backend.Hosting",font_size="4em"  ),
            pc.html('<h1 style="font-size:4em; font-weight: bold;   background: rgb(117,106,238);  background: linear-gradient(90deg, rgba(117,106,238,1) 33%, rgba(238,117,106,1) 100%);   -webkit-background-clip: text;   -webkit-text-fill-color: transparent;">Pure Python</h1>'),
            pc.text("Build web apps in minutes. Deploy with a single command.", font_size="1.5em",color="#989898"),
            pc.hstack(
                pc.input(placeholder="Your email address",width="300px"),
                pc.button("Stay Updated!", background_color="black",color="white"),
            spacing="40px"
            ),
         ),
        padding_top="10%",
       
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
