import typer
from rich import print

app = typer.Typer()


@app.command()
def create(text: str):
    print(f"Text: {text}")


@app.command()
def version():
    print("\nQR Generator CLI")
    print("[bold magenta]v0.0.1[/bold magenta]")


if __name__ == "__main__":
    app()
