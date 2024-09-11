'''Command Parser Module'''

from monster_fight import MonsterFight
from inventory import Inventory
from inventory import Item

class CommandParser:
    def __init__(self, inventory, status):
        self.inventory = inventory
        self.status = status
        self.fight = MonsterFight(inventory)

    def parse(self, command, game_places):
        '''Parse the command from user input to main and perform the appropriate action'''
        command = command.lower()

        '''Handle Sage quest at beginning of game'''
        if 'speak to sage' in command and self.status.get_state() == 'Village of Arion Part 1':
            story, image = self.status.update_state('Speak to Sage')
            return story, image
        
        '''Handle Begin Quest after speaking to sage'''
        if 'begin quest' in command and self.status.get_state() == 'Sage Quest':
            sword_of_arundil = Item('Sword of Arundil', 50)
            shield = Item('Shield', 40)
            self.inventory.add_item(sword_of_arundil)
            self.inventory.add_item(shield)
            story, image = self.status.update_state('Begin Quest')
            return story, image 
        
        if 'north' in command or 'south' in command:
            story, image = self.status.update_state(command.capitalize())
            return story, image

        if 'fight' in command:
            enemy_type = self.status.game_places[self.status.get_state()].get('Enemy', None)
            if enemy_type:
                return self.fight.start_fight(enemy_type), None
            else:
                return "There is no enemy here to fight.", None

        if 'inventory' in command:
            return self.inventory.show_inventory(), None

        return "Unknown Command!", None