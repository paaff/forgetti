import click
import pickle
import item
from datetime import date, datetime


@click.group()
def cli():
    pass


@click.command(help='Add a new note.')
@click.argument('group', type=click.STRING, required=True)
@click.argument('note', type=click.STRING, required=True)
@click.option('--deadline', '-d', type=click.STRING, help='Deadline in format "date-month", e.g. 23-06')
def add(note, group, deadline):
    if deadline != None:
        d = datetime.strptime(deadline, "%d-%m").date()
        d = d.replace(year=date.today().year) 
        item.make_item(note, group, d)

    else:
        item.make_item(note, group, date(date.today().year, 12, 31))


@click.command(help='Query existing notes by group. If no group is specified, all notes are included.')
@click.option('--group', '-g', type=click.STRING, help='Specify a group to filter notes on.')
def query(group):


    # Load from data file if it exist.
    try:
        items = pickle.load(open(item.FILENAME, "rb"))
        # Sort in respect to dates.
        items.sort(key=lambda item: item.deadline)
        
        # Is a group specified?
        if (group):
            filtered_groups = list(filter(lambda x: x.group == group, items))
            show(filtered_groups)
 
        else:
            show(items)

    except (FileNotFoundError):
       print('Error, no notes found.')


def show(items):
    click.echo('Notes remembered by forgetti: ', nl=False)
    click.secho('{}\n'.format(len(items)), fg='magenta')
    
    for index, item in enumerate(items):
        click.secho('    {}. ({}): '.format(index, item.group), fg='blue', nl=False)
        click.secho('{}'.format(item.note), fg='white')
        click.echo('    Forgetti deadline: ', nl=False)
        click.secho('{}\n'.format(item.deadline), fg='green')       


cli.add_command(add)
cli.add_command(query)

if __name__ == "__main__":
    cli()