# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def inventory(self):
        if len(self.items) == 0:
            print('Nothing in your inventory')
        else:
            output = f'This is your current inventory: '
            for i in self.items:
                output += f' {i.name} '
            print(output)

    def getItem(self, item):
        for i in self.current_room.items:
            if i.name == item:
                self.items.append(i)
                self.current_room.items.remove(i)
                print(f'{self.name} has picked up {item}')

    def dropItem(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                print(f'{i.name} was removed')
