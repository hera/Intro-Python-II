import sys
import random
from room import Room
from player import Player
import item

# Declare all the rooms

room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    "treasure": Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


item_classes = [item.Coin, item.Gem, item.Knife, item.Stone, item.Sword]
items = []


# Generate random quantity of items

for c in item_classes:
    for i in range(random.randint(0, 3)):
        items.append(c())


# Randomize items

random.shuffle(items)


# Put items in rooms
for r in room:
    for i in items:
        if not len(items):
            break
        room[r].add_item(items.pop())


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def print_help():
    print(
        """
        Commands:

        n - go north
        e - go east
        s - go south
        w - go west

        whereami - display current location

        h, help  - display this message
        q, quit  - quit
        """
    )


def go(direction):
    if direction == "n":
        if not user.current_room.n_to:
            print("Can't go north.")
        else:
            user.current_room = user.current_room.n_to
            print(user.current_room)
            user.current_room.show_items()
    elif direction == "e":
        if not user.current_room.e_to:
            print("Can't go east.")
        else:
            user.current_room = user.current_room.e_to
            print(user.current_room)
            user.current_room.show_items()
    elif direction == "s":
        if not user.current_room.s_to:
            print("Can't go south.")
        else:
            user.current_room = user.current_room.s_to
            print(user.current_room)
            user.current_room.show_items()
    elif direction == "w":
        if not user.current_room.w_to:
            print("Can't go west.")
        else:
            user.current_room = user.current_room.w_to
            print(user.current_room)
            user.current_room.show_items()
    else:
        print("Unknown direction.")



if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
    print_help()
    quit()

print(
    """
    Welcome to Digital Adventure
    ______________________________________________
    """
)

# Ask name

while True:
    entered_name = input("Please enter your name: ")
    
    if entered_name in ("q", "quit"):
        quit()
    elif entered_name == "":
        entered_name = "Anonymous Adventurer"
    
    user = Player(entered_name, room["outside"])
    print(f"Welcome, {user.name}!\n")
    print(user.current_room)
    user.current_room.show_items()

    if user.name:
        break


while True:
    command = input(">>> ").split(" ")
    
    if command[0] in ("q", "quit"):
        quit()
    elif command[0] in ("h", "help"):
        print_help()
    elif command[0] == "whereami":
        print(user.current_room)
        user.current_room.show_items()
    elif command[0] == "n":
        go("n")
    elif command[0] == "e":
        go("e")
    elif command[0] == "s":
        go("s")
    elif command[0] == "w":
        go("w")
    else:
        print("Incorrect command.")