'''Command Parser Module'''

from inventory import Inventory
from monster_fight import MonsterFight
from status import Status

class CommandParser:
    def __init__(self):
        self.inventory = Inventory()
        self.status = Status()
        self.fight = MonsterFight()

    def parse(self, command, game_state, game_places):
        '''Parse the command from user input to main and perform the appropriate action'''
        command = command.lower()
        
        if 'north' in command or 'south' in command:
            return command.capitalize()
        
        elif 'fight' in command:
            enemy_type = game_places[game_state].get('Enemy', None)
            if enemy_type:
                return self.fight.start_fight(enemy_type)
            else:
                return "There is no enemy here to fight."
        
        elif 'inventory' in command:
            return self.inventory.show_inventory()
        
        elif 'status' in command:
            return self.status.show_status()
        
        else:
            return "Unknown Command!"