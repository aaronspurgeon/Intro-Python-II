# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.n_to = None

    def __str__(self):
        output = f'Items here: '
        for item in self.items:
            output += f'{item.name}'
        # if self.s_to:
        #     output += 'To the south is: ' + self.s_to.name + '\n'
        # if self.e_to:
        #     output += 'To the south is: ' + self.s_to.name + '\n'
        # if self.w_to:
        #     output += 'To the south is: ' + self.s_to.name + '\n'
        # if self.n_to:
        #     output += 'To the south is: ' + self.s_to.name + '\n'
        return output
