"""
Import Modules
"""
import PySimpleGUI as sg
from command_parser import CommandParser

"""
Initialize game state at starting point and other components
"""
game_state = 'Village of Arion'
parser = CommandParser()

"""
Game Places with descriptions and connections
"""

game_places = {
    'Village of Arion Part 1': {
        'Story': 'You are in the peaceful Village of Arion, the smell of fresh bread and the bustle of the market fills your senses with a feeling of comfort, then an old sage approaches. . . .',
        'North': 'Whispering Forest', 
        'South': 'Temple of Ages', 
        'Image': 'village image',
        'Enemy': None
    },
    'Village of Arion Part 2': {
        'Story': 'You have received the Sword of Arundil and Shield, paths out of the village lead North (Whispering Forest) and South (Temple of Ages).',
        'North': 'Whispering Forest Part 1', 
        'South': 'Village of Arion', 
        'Image': 'village of arion image',
        'Enemy': None
    },
    'Whispering Forest Part 1': {
        'Story': 'You arrive at the overgrown entrance to the Whispering Forest. Paths lead to the north (Deeper into the forest) and south (Village of Arion).',
        'North': 'Whsipering Forest Part 2', 
        'South': 'Village of Arion', 
        'Image': 'whispering_forest_image_1',
        'Enemy': None
    },
    'Whispering Forest Part 2': {
        'Story': 'You venture deeper into the Whispering Forest, a shadowy figure lurks in the distance, you clear some vegetation out of the way and can continue further north (Heart of the Forest) or south (Back towards Village of Arion).',
        'North': 'Whispering Forest Part 3', 
        'South': 'Whispering Forest Part 1', 
        'Image': 'whispering_forest_image_2',
        'Enemy': None
    },
    'Whispering Forest Part 3': {
        'Story': 'You have reached the heart of the Whispering Forest. Strange creatures can be heard in the darkness, then out of the trees, a Dark Rider Approaches. Prepare to Fight!',
        'Fight': 'initiate_fight', 
        'South': 'Whispering Forest Part 2', 
        'Image': 'whispering_forest_image_3',
        'Enemy': 'Dark Rider'
    },
}

def initiate_fight():
    '''Placeholder for fight module logic'''
    return "A fight has begun with the enemy! (Fight module placeholder)"

def show_current_place():
    '''Displays the current location in game_state'''
    return game_places[game_state]['Story']

def game_play(action):
    '''Updates the game state based on player action'''
    global game_state

    if action == 'North' or action == 'South':
        next_place = game_places[game_state].get(action, '')
        if next_place:
            game_state = next_place
            return f'Moving {action}...\n' + show_current_place()
        else:
            return f'You cant go {action} from here.'
    elif action == 'Fight' and 'Fight' in game_places[game_state]:
        '''Trigger Fight via the key in the dictionary'''
        return initiate_fight()
    return 'Invalid action.'

def make_game_window():
    '''Creates the PySimplueGUI game window'''
    sg.theme('Dark Blue 3')

    '''Get the image from the game_state location'''
    current_image = game_places[game_state]['Image']

    '''Layout for game window'''
    layout = [
        [sg.Image(current_image, size=(100, 100), key='-IMG-')],
        [sg.Text(show_current_place(), size=(40, 5), key='-OUTPUT-')],
        [sg.Input(key='-IN-', size=(20, 1))],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]

    return sg.Window('Legend of the Sacred Forest', layout)

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
            window['-IMG-'].update(game_places[game_state]['Image'])

    window.close()

if __name__ == '__main__':
    main()