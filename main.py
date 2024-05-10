import typer
from rich import print
from typing_extensions import Annotated

from app.qr_code import QRCode


app = typer.Typer()


@app.command()
def create(
        text: str,
        filename: Annotated[str, typer.Option(help="QR filename.")] = "qr",
        border: Annotated[int, typer.Option(help="Border size of the QR.")] = 1,
        scale: Annotated[int, typer.Option(help="Size of the QR.")] = 25,
):
    try:
        qr = QRCode(filename=filename, border=border, scale=scale)
        qr_path = qr.generate(text)

        print(f"QR generated in [bold]{qr_path}[/bold]")
    except Exception as e:
        print(f"[red]Error generating the QR: {e}[/red]")


@app.command()
def version():
    print("\nQR Generator CLI")
    print("[bold magenta]v0.0.1[/bold magenta]")


if __name__ == "__main__":
    app()
