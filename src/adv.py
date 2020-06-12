from room import Room
from player import Player
from items import Item

# rooms items
torch = Item('Torch', 'A simple torch, seems to be losing its burn quickly')
compass = Item(
    'Compass', 'Dirt covered compass, seems to have been here awhile.')
flask = Item(
    'Flask', 'A jeweled covered flask, there seems to be bit of foul smelling liquid at the bottom')
helmet = Item(
    'Helmet', 'A broken helmet, the aged leather gives it an ancient look')
coin = Item(
    'Coin', 'A lone gold coin found by the exit. Whoever looted this place left in a hurry.')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [torch]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [compass]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [flask]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [helmet]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [coin]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
aaron = Player("Aaron", room['outside'])


# Write a loop that:

# functions


def location():
    print('Type (q) to quit')
    print(f'{aaron.name} is currently in {aaron.current_room.name}')
    print(f'{aaron.current_room.description}')
    print(aaron.current_room)


aaron.inventory()

# while True:
#     location()
#     choice = input('Enter a direction: ')

#     if choice in {'n', 's', 'e', 'w'}:
#         try:
#             hasattr(aaron.current_room, f'{choice}_to')
#             aaron.current_room = getattr(
#                 aaron.current_room, f'{choice}_to')
#         except AttributeError:
#             print('Please select a valid direction')
#     if (choice == 'q'):
#         break


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
