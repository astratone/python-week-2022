import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print

from beerlog.core import add_beer_to_database, get_beers_from_database


main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command("add")
def add(
        name: str,
        style: str,
        flavor: int = typer.Option(...),
        image: int = typer.Option(...),
        cost: int = typer.Option(...)
):
    """Adds anew beer to database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print(":beer_mug: Beer added to database.")
    else:
        print(":no_entry: - Cannot add beer.")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database"""
    beers = get_beers_from_database(style)
    table = Table(title="Beerlog Database" if not style else f"Beerlog {style}")
    headers = ["id", "name", "style", "flavor", "image", "cost", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%d-%m-%Y")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


