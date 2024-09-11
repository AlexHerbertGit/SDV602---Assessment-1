'''Command Parser Module'''

from monster_fight import MonsterFight
from status import Status
from inventory import Inventory
from inventory import Item

class CommandParser:
    def __init__(self, inventory):
        self.inventory = Inventory()
        self.status = Status()
        self.fight = MonsterFight()

    def parse(self, command, game_state, game_places):
        '''Parse the command from user input to main and perform the appropriate action'''
        command = command.lower()

        '''Handle Sage quest at beginning of game'''
        if game_state == 'Village of Arion Part 1' and 'speak to sage' in command:
            game_state == game_places[game_state].get('Speak to Sage', None)
            return game_places[game_state]['Story'], game_state
        
        '''Handle Begin Quest after speaking to sage'''
        if game_state == 'Sage Quest' and 'begin quest' in command:
            '''Give Player sword of arundil and shield when beginning quest'''
            sword_of_arundil = Item('Sword of Arundil', 50)
            shield = Item('Shield', 40)
            self.inventory.add_item(sword_of_arundil)
            self.inventory.add_item(shield)
            game_state = game_places[game_state].get('Begin Quest', None)
            return f'The sage has given you the Sword of Arundil and Shield.', game_state

        if 'north' in command or 'south' in command:
            return command.capitalize()
        
        elif 'speak to sage' in command:
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