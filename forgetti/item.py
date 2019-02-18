# Collection of objects
# TODO: Probs a map structure instead
items = []

# Objects representing what to remember.
class Item(object):
    title = ""
    group = ""

    def __init__(self, title, group):
        self.title = title
        self.group = group

def make_item(title, group):
    fresh = Item(title, group)
    items.append(fresh)