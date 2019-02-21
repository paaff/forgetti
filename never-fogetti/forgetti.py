from item import make_item, items
import click

@click.group()
def cli():
        pass

@click.command()
@click.option('-a', '--add', help='Add a new note.')
def add():    
    title = raw_input("What do you want to remember?")
    group = raw_input("Which group should it be assigned to?")
    make_item(title, group)

@click.command()
@click.option('-q', '--query', help='Query a note by group.')
def query():
    print("Listing all items.")
    for item in items:
        print(item.title)

@click.command()
@click.option('-s', '--status', help='Get status of all the notes.')
def status():
        print('yep, havent done anything')

# Add commands to cli
cli.add_command(add)
cli.add_command(query)
cli.add_command(status)

#if __name__ == "__main__":
#        cli()
