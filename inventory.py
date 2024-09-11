'''Inventory Module'''

class Item:
    def __init__(self, name, value):
        '''Create items with a name and value'''
        self.name = name
        self.value = value

    def __str__(self):
        return f'{self.name} (Value: {self.value})'
    
class Inventory:
    def __init__(self):
        '''Initialize an empty inventory using a list'''
        self.items = []

    def add_item(self, item):
        '''Add an item from the inventory'''
        self.items.append(item)
        return f'{item.name} has been added to your inventory.'
    
    def remove_item(self, item_name):
        '''Remove item from the inventory'''
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return f'{item_name} has been removed from your inventory.'
            return f'{item_name} is not in the inventory'
        
    def show_inventory(self):
        '''Display the current items in the player inventory'''
        if self.items:
            return 'Inventory:\n' + '\n'.join([str(item) for item in self.items])
        else:
            return 'Your inventory is empty.'
        
    def use_item(self, item_name):
        '''Use an item from the inventory'''
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return f'You used {item.name}.'
        return f'{item_name} is not available in your inventory.'
    