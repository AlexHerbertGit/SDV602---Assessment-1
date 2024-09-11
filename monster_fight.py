'''Monster Fight Module'''

from random import randint
from inventory import Inventory

class MonsterFight:
    def __init__(self, inventory):
        self.player_health = 100
        self.enemy_health = 0
        self.enemy_type = None
        self.in_fight = False
        self.inventory = inventory

    def start_fight(self, enemy_type):
        '''Initialize fight with specified enemy'''
        self.enemy_type = enemy_type

        if enemy_type == 'Dark Rider':
           self.enemy_health = 100
        elif enemy_type == 'Boneguard':
            self.enemy_health = 100
        else:
            self.enemy_health = 40

        self.in_fight = True
        return f"a {enemy_type} apprears! Prepare to fight! Choose 'Attack' or 'Inventory."
        
    def fight_action(self, action):
        fight_log = []

        if action == 'attack':
            '''Players turn to attack'''
            player_attack = randint(20, 30)
            self.enemy_health -= player_attack
            fight_log.append(f'You hit the {self.enemy_type} for {player_attack} damage. Enemy health: {self.enemy_health}')

            if self.enemy_health <= 0:
                fight_log.append(f'You have defeated the {self.enemy_type}!')
                self.in_fight = False
                return '\n'.join(fight_log)

            '''Enemy's Turn to attack'''
            enemy_attack = randint(15, 25)
            self.player_health -= enemy_attack
            fight_log.append(f'The {self.enemy_type} hits you for {enemy_attack} damage. Your health: {self.player_health}')

            if self.player_health <= 0:
                fight_log.append(f'You have been defeated by the {self.enemy_type}....')
                self.in_fight = False
                return '\n'.join(fight_log)

            return '\n'.join(fight_log)
        
        elif action == 'inventory':
            return self.inventory.show_inventory() + "\n Type 'use <item>' to use an item."
        
        else:
            return "Invalid Action! Type 'Attack' or 'Inventory'."
    
    def use_item(self, item_name):
        '''Use an item from the inventory'''
        if item_name.lower() == 'health elixir' and 'Health Elixir' in self.inventory.items:
            self.player_health += 30
            self.inventory.remove_item('Health Elixir')
            return f'You used a Health Elixir and restored 30 health! Current Health: {self.player_health}'
        else:
            return f'{item_name} is not available in inventory.'    
