from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

print(room['outside'].n_to.name)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
aaron = Player("Aaron", room['outside'])


# Write a loop that:
choice = 'n'
print('Type (q) to quit')
print(f'{aaron.name} is currently in {aaron.current_room.name}')
print(f'{aaron.current_room.description}')


def location():
    print(f'{aaron.name} is currently in {aaron.current_room.name}')
    print(f'{aaron.current_room.description}')


while True:

    if aaron.current_room.name == 'Outside Cave Entrance':
        choice = input(
            'Please select (n) to head into the Foyer: ')
    elif aaron.current_room.name == 'Foyer':
        choice = input(
            'Select (n) to venture to the Overlook or select (e) to explore the Narrow. Otherwise select (s) to go back: ')
    elif aaron.current_room.name == 'Grand Overlook':
        choice = input(
            'Please select (s) to head back into the Foyer: ')
    elif aaron.current_room.name == 'Narrow Passage':
        choice = input(
            'Please select (w) to head into the Foyer or select (n) to head to the Treasure room: ')
    else:
        choice = input(
            'Please select (s) to head into the Narrow: ')

    try:
        if (choice == 'q'):
            break
        if (aaron.current_room.name == 'Outside Cave Entrance' and choice == 'n'):
            aaron.current_room = room['foyer']
            location()
        elif (aaron.current_room.name == 'Foyer' and choice == 'n'):
            aaron.current_room = room['overlook']
            location()
        elif (aaron.current_room.name == 'Foyer' and choice == 'e'):
            aaron.current_room = room['narrow']
            location()
        elif (aaron.current_room.name == 'Foyer' and choice == 's'):
            aaron.current_room = room['outside']
            location()
        elif (aaron.current_room.name == 'Grand Overlook' and choice == 's'):
            aaron.current_room = room['foyer']
            location()
        elif (aaron.current_room.name == 'Narrow Passage' and choice == 'w'):
            aaron.current_room = room['foyer']
            location()
        elif (aaron.current_room.name == 'Narrow Passage' and choice == 'n'):
            aaron.current_room = room['treasure']
            location()
        elif (aaron.current_room.name == 'Treasure Chamber' and choice == 's'):
            aaron.current_room = room['narrow']
            location()

    except ValueError:
        print('Please select a valid directional movement')
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
