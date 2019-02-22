import click
import pickle
from item import make_item


@click.group()
def cli():
    pass


@click.command(help='Add a new note.')
@click.argument('group', type=click.STRING, required=True)
@click.argument('note', type=click.STRING, required=True)
def add(note, group):
    make_item(note, group)


@click.command(help='Query existing notes by group.')
@click.argument('group', type=click.STRING)
def query(group):
    # Load from data file if it exist.
    try:
       items = pickle.load(open("notes.data", "rb"))
    except (FileNotFoundError):
       print('Error, no notes found.')

    for i in items:
        click.echo(i.note)


cli.add_command(add)
cli.add_command(query)

if __name__ == "__main__":
     cli()
