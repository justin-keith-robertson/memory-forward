from typer import Typer
from memory_forward.commands import hello
from memory_forward.commands import goodbye
from memory_forward.commands import organize

app = Typer()
app.command()(hello.hello)
app.command()(goodbye.goodbye)
app.command()(organize.organize)

def main():
    app()
