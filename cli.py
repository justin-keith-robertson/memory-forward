from typer import Typer
from app import hello
from app import goodbye

app = Typer()
app.command()(hello.hello)
app.command()(goodbye.goodbye)

def cli():
    app()

if __name__ == "__main__":
    cli()
