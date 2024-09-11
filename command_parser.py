'''Command Parser Module'''

from monster_fight import MonsterFight
from inventory import Inventory
from inventory import Item

class CommandParser:
    def __init__(self, inventory):
        self.inventory = inventory
        self.fight = MonsterFight(inventory)

    def parse(self, command, game_state, game_places):
        '''Parse the command from user input to main and perform the appropriate action'''
        command = command.lower()

        '''Handle Sage quest at beginning of game'''
        if game_state == 'Village of Arion Part 1' and 'speak to sage' in command:
            game_state = game_places[game_state].get('Speak to Sage', None)
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
            return command.capitalize(), game_state
        
        elif 'speak to sage' in command:
            return command.capitalize(), game_state
        
        elif 'fight' in command:
            enemy_type = game_places[game_state].get('Enemy', None)
            if enemy_type:
                return self.fight.start_fight(enemy_type), game_state
            else:
                return "There is no enemy here to fight.", game_state
        
        elif 'inventory' in command:
            return self.inventory.show_inventory(), game_state
        
        else:
            return "Unknown Command!", game_state