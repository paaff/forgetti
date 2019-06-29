import pickle
import time
from datetime import date 

FILENAME = ".notes.forgetti"

class Item(object):
    note = ""
    group = ""
    deadline = ""

    def __init__(self, note, group, deadline):
        self.note = note
        self.group = group
        self.deadline = deadline


def make_item(note, group, deadline):
    items = []

    # Load from data file if it exist.
    try:
       items = pickle.load(open(FILENAME, "rb"))
    except (FileNotFoundError):
        # Alright to fail, just means this it the first note.
        pass

    fresh = Item(note, group, deadline)
    items.append(fresh)

    # Save the notes
    pickle.dump(items, open(FILENAME, "wb"))