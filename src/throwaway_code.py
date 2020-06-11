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
        else:
            print('Please enter a valid directional movement')
