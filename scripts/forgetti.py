import click
import pickle
from item import make_item
from datetime import date, datetime


@click.group()
def cli():
    pass


@click.command(help='Add a new note.')
@click.argument('group', type=click.STRING, required=True)
@click.argument('note', type=click.STRING, required=True)
@click.option('--deadline', '-d', type=click.STRING, help='Deadline in format "date-month", e.g. 23-06')
def add(note, group, deadline):
    d = datetime.strptime(deadline, "%d-%m").date()
    d = d.replace(year=date.today().year)
    
    make_item(note, group, d)


@click.command(help='Query existing notes by group.')
@click.argument('group', type=click.STRING)
def query(group):
    # Load from data file if it exist.
    try:
       items = pickle.load(open("notes.data", "rb"))
    except (FileNotFoundError):
       print('Error, no notes found.')

    # Sort in respect to dates.
    items.sort(key=lambda item: item.deadline)
    filtered_groups = list(filter(lambda x: x.group == group, items))
    show(filtered_groups)
    


def show(items):
   click.echo('Current notes in database: ', nl=False)
   click.secho('{}'.format(len(items)), fg='magenta')

   for i in items:
      click.echo('Note: {}, Group: {}, Deadline: {}'.format(i.note, i.group, i.deadline))
   



cli.add_command(add)
cli.add_command(query)

if __name__ == "__main__":
    cli()
