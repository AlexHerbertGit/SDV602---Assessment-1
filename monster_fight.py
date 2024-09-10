'''Monster Fight Module'''

from random import randint
from inventory import Inventory

class MonsterFight:
    def __init__(self):
        self.player_health = 100
        self.inventory = Inventory()

    def start_fight(self, enemy_type):
        if enemy_type == 'Dark Rider':
           enemy_health = 100
        elif enemy_type == 'Boneguard':
            enemy_health = 100
        else:
            enemy_health = 40
    
        fight_log = []
        fight_log.append(f"A {enemy_type} appears! Prepare to fight!")

        while self.player_health > 0 and enemy_health > 0:
            '''Players turn to attack'''
            player_attack = randint(20, 30)
            enemy_health -= player_attack
            fight_log.append(f'You hit the {enemy_type} for {player_attack} damage. Enemy health: {enemy_health}')

            if enemy_health <= 0:
                fight_log.append(f'You have defeated the {enemy_type}!')
                break

            '''Enemy's Turn to attack'''
            enemy_attack = randint(15, 25)
            self.player_health -= enemy_attack
            fight_log.append(f'The {enemy_type} hits you for {enemy_attack} damage. Your health: {self.player_health}')

            if self.player_health <= 0:
                fight_log.append(f'You have been defeated by the {enemy_type}....')
                break

        return '\n'.join(fight_log)
    
