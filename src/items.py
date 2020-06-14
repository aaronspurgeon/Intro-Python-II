class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Equip_armor(Item):
    def __init__(self, name, description, plus_def, plus_hp):
        super().__init__(name, description)
        self.plus_def = plus_def
        self.plus_hp = plus_hp


class Equip_trinkets(Item):
    def __init__(self, name, description, plus_hp, plus_atk):
        super().__init__(name, description)
        self.plus_hp = plus_hp
        self.plus_atk = plus_atk
