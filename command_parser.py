'''Command Parser Module'''

from inventory import Inventory
from monster_fight import MonsterFight
from status import Status

class CommandParser:
    def __init__(self):
        self.inventory = Inventory()
        self.status = Status()
        self.fight = MonsterFight()

    def parse(self, command, game_state):
        '''Parse the command from user input to main and perform the appropriate action'''
        command = command.lower()
        if 'north' in command or 'south' in command:
            return command.capitalize()
        
        elif 'fight' in command:
            return self.fight.start_fight()
        
        elif 'inventory' in command:
            return self.inventory.show_inventory()
        
        elif 'status' in command:
            return self.status.show_status()
        
        else:
            return "Unknown Command!"