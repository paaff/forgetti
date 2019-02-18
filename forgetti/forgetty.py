from item import make_item, items

def greet():
    print("You currently have X items in your forgetti vault!")

def add():    
    title = raw_input("What do you want to remember?")
    group = raw_input("Which group should it be assigned to?")
    
    make_item(title, group)

def query():
    print("Listing all items.")
    for item in items:
        print(item.title)

if __name__ == "__main__":
    greet()