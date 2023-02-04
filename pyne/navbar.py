import pynecone as pc


def navbar():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.image(src="/logo.png", width="40px"),
                pc.heading("Pynecone",font_size="20px"), 
            ),
            pc.input(width="400px",placeholder="Search the docs"),
            pc.hstack(
               pc.link("Docs",font_size="20px",href="/docs"),
               pc.link("Gallery",font_size="20px"),
               pc.link("References",font_size="20px"),
               pc.image(src="/github.png",width="20px"),
               spacing="20px"
            ),
            justify="space-between",
            border_bottom="1px solid #F0F0F0",
            padding_x="4em",
            padding_y="1em",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )