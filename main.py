"""
Import Modules
"""
import PySimpleGUI as sg


"""
Initialize game state and other components
"""
game_state = 'Village of Arion'

"""
Game Places with descriptions and connections
"""

game_places = {
    'Village of Arion Part 1': {
        'Story': 'You are in the peaceful Village of Arion, the smell of fresh bread and the bustle of the market fills your senses with a feeling of comfort, then an old sage approaches. . . .',
        'North': 'Whispering Forest', 'South': 'Temple of Ages', 'Image': 'village image'
    },
    'Village of Arion Part 2': {
        'Story': 'You have received the Sword of Arundil and Shield, paths out of the village lead North (Whispering Forest) and South (Temple of Ages).',
        'North': 'Whispering Forest Part 1', 'South': 'Village of Arion', 'Image': 'village of arion image'
    },
    'Whispering Forest Part 1': {
        'Story': 'You arrive at the overgrown entrance to the Whispering Forest. Paths lead to the north (Deeper into the forest) and south (Village of Arion).',
        'North': 'Whsipering Forest Part 2', 'South': 'Village of Arion', 'Image': 'whispering_forest_image_1'
    },
    'Whispering Forest Part 2': {
        'Story': 'You venture deeper into the Whispering Forest, a shadowy figure lurks in the distance, you clear some vegetation out of the way and can continue further north.',
        'North': 'Whispering Forest Part 3', 'South': 'Whispering Forest Part 1', 'Image': 'whispering_forest_image_2'
    },
    'Whispering Forest Part 3': {
        'Story': 'You have reached the heart of the Whispering Forest. Strange creatures can be heard in the darkness, then out of the trees, a Dark Rider Approaches. Prepare to Fight!',
        'Fight': 'initiate_fight', 
        'South': 'Whispering Forest Part 2', 'Image': 'whispering_forest_image_3'
    },
}