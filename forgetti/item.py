import pickle

# Collection of objects
items = []

class Item(object):
    note = ""
    group = ""

    def __init__(self, note, group):
        self.note = note
        self.group = group


def make_item(note, group):
    fresh = Item(note, group)
    items.append(fresh)

    # Save the notes
    pickle.dump(items, open("notes.data", "wb"))