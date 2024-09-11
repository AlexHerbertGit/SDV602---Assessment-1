"""
Import Modules
"""
import PySimpleGUI as sg
from command_parser import CommandParser
from inventory import Inventory, Item

"""
Initialize game state at starting point and other components
"""
inventory = Inventory()
game_state = 'Village of Arion Part 1'
parser = CommandParser(inventory)

"""
Initialize Game Items
"""

health_elixir = Item('Health Elixir', 30)
sacred_relic = Item('Sacred Relic', 1)

"""
Game Places with descriptions and connections to other locations/actions
"""

game_places = {
    'Village of Arion Part 1': {
        'Story': 'You are in the peaceful Village of Arion, the smell of fresh bread and the bustle of the market fills your senses with a feeling of comfort, then an old sage approaches. . . .( type "speak to sage" )',
        'North': '', 
        'South': '', 
        'Speak to Sage': 'Sage Quest',
        'Image': 'images/village_of_arion_pt1.png',
        'Enemy': None
    },
    'Sage Quest': {
        'Story': 'The sage says: "Hello young adventurer, Malakar has taken control of the land, it is up to you to save us from him. Take this Sword of Arundil and Shield to help you on your quest! ( type "begin quest" )',
        'North': '', 
        'South': '',
        'Begin Quest': 'Village of Arion Part 2',
        'Image': 'images/sage_quest.png',
        'Enemy': None
    },
    'Village of Arion Part 2': {
        'Story': 'You have received the Sword of Arundil and Shield, paths out of the village lead North (Whispering Forest) and South (Temple of Ages).',
        'North': 'Whispering Forest Part 1', 
        'South': 'Temple of Ages', 
        'Image': 'images/village_of_arion_pt2.png',
        'Enemy': None
    },
    'Whispering Forest Part 1': {
        'Story': 'You arrive at the overgrown entrance to the Whispering Forest. Paths lead to the north (Deeper into the forest) and south (Village of Arion).',
        'North': 'Whsipering Forest Part 2', 
        'South': 'Village of Arion', 
        'Image': 'images/whispering_forest_pt1.png',
        'Enemy': None
    },
    'Whispering Forest Part 2': {
        'Story': 'You venture deeper into the Whispering Forest, a shadowy figure lurks in the distance, you clear some vegetation out of the way and can continue further north (Heart of the Forest) or south (Back towards Village of Arion).',
        'North': 'Whispering Forest Part 3', 
        'South': 'Whispering Forest Part 1', 
        'Image': 'images/whispering_forest_pt2.png',
        'Enemy': None
    },
    'Whispering Forest Part 3': {
        'Story': 'You have reached the heart of the Whispering Forest. Strange creatures can be heard in the darkness, then out of the trees, a Dark Rider Approaches. Prepare to Fight!',
        'Fight': 'initiate_fight', 
        'South': 'Whispering Forest Part 2', 
        'Image': '.images/whispering_forest_pt3.png',
        'Enemy': 'Dark Rider'
    },
}

def initiate_fight():
    '''Placeholder for fight module logic'''
    return "A fight has begun with the enemy! (Fight module placeholder)"

def show_current_place():
    '''Displays the current location in game_state'''
    return game_places[game_state]['Story']

def make_game_window():
    '''Creates the PySimplueGUI game window'''
    sg.theme('Dark Blue 3')

    '''Get the image from the game_state location'''
    current_image = game_places[game_state]['Image']


    left_column = [
        [sg.Image(filename=current_image, key='-IMG-', size=(700, 700))]
    ]

    right_column = [
        [sg.Text(show_current_place(), size=(60, 10), key='-OUTPUT-')],
        [sg.Input(key='-IN-', size=(40, 1))],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]

    '''Layout for game window'''
    layout = [
        [sg.Column(left_column), sg.Column(right_column)]
    ]

    
    return sg.Window('Legend of the Sacred Forest', layout, size=(1280, 720), finalize=True)

def main():

    '''Main game loop logic and window creation'''
    window = make_game_window()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Submit':
            user_input = values['-IN-']
            '''User input processing with parser'''
            output = parser.parse(user_input, game_state, game_places)

            '''Update the game display'''
            window['-OUTPUT-'].update(output)
            window['-IMG-'].update(filename=game_places[game_state]['Image'])

    window.close()

if __name__ == '__main__':
    main()