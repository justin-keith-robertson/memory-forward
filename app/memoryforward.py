from typer import Typer
import hello
import goodbye

app = Typer()
app.command()(hello.hello)
app.command()(goodbye.goodbye)

def cli():
    app()
