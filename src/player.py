# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, defense, hp, atk):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.hp = 100
        self.defense = 0
        self.atk = 0

    def __str__(self):
        return f'hp: {self.hp}, def: {self.defense}, atk: {self.atk}'

    def inventory(self):
        if len(self.items) == 0:
            print('Nothing in your inventory')
        else:
            output = f'This is your current inventory: '
            for i in self.items:
                output += f' {i.name} '
                # if i.plus_def > 0 and i.plus_hp > 0:
                #     self.defense = self.defense + i.plus_def
                #     self.hp = self.hp + i.plus_hp
                # else:
                #     print(f'def: {i.plus_def}')

            print(output)

    def getItem(self, item):
        for i in self.current_room.items:
            if i.name == item:
                self.items.append(i)
                self.current_room.items.remove(i)
                print(f'{self.name} has picked up {item}')
                if hasattr(i, 'plus_def'):
                    self.defense = i.plus_def + self.defense
                    self.hp = i.plus_hp + self.hp
                elif hasattr(i, 'plus_atk'):
                    self.hp = i.plus_hp + self.hp
                    self.atk = i.plus_atk + self.atk

    def dropItem(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                self.current_room.items.append(i)
                print(f'{i.name} was dropped. Its where you left it.')
                if hasattr(i, 'plus_def'):
                    self.defense = self.defense - i.plus_def
                    self.hp = self.hp - i.plus_hp
                elif hasattr(i, 'plus_atk'):
                    self.hp = self.hp - i.plus_hp
                    self.atk = self.atk - i.plus_atk
