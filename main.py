"""
Import Modules
"""
import PySimpleGUI as sg
from command_parser import CommandParser
from inventory import Inventory, Item
from status import Status

"""
Game Places with descriptions and connections to other locations/actions
"""

game_places = {
    'Village of Arion Part 1': {
        'Story': 'You are in the peaceful Village of Arion, the smell of fresh bread and the bustle of the market fills your senses with a feeling of comfort, then an old sage approaches. . . .\n( type "speak to sage" )',
        'North': '', 
        'South': '', 
        'Speak to Sage': 'Sage Quest',
        'Image': 'images/village_of_arion_pt1.png',
        'Enemy': None
    },
    'Sage Quest': {
        'Story': 'The sage says: "Hello young adventurer, Malakar has taken control of the land, it is up to you to save us from him. Take this Sword of Arundil and Shield to help you on your quest! \n( type "begin quest" )',
        'North': '', 
        'South': '',
        'Begin Quest': 'Village of Arion Part 2',
        'Image': 'images/sage_quest.png',
        'Enemy': None
    },
    'Village of Arion Part 2': {
        'Story': 'You have received the Sword of Arundil and Shield, paths out of the village lead North (Whispering Forest) and South (Temple of Ages).',
        'North': 'Whispering Forest Part 1', 
        'South': 'Temple of Ages Part 1', 
        'Image': 'images/village_of_arion_pt2.png',
        'Enemy': None
    },
    'Whispering Forest Part 1': {
        'Story': 'You arrive at the overgrown entrance to the Whispering Forest. Paths lead to the north (Deeper into the forest) and south (Village of Arion).',
        'North': 'Whispering Forest Part 2', 
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
        'Story': 'You have reached the heart of the Whispering Forest. Strange creatures can be heard in the darkness, then out of the trees, a Dark Rider Approaches. \n( type "fight" to start the battle )',
        'Fight': 'start_fight()', 
        'South': 'Whispering Forest Part 2', 
        'Image': 'images/whispering_forest_pt3.png',
        'Enemy': 'Dark Rider',
        'Continue': 'Whispering Forest Part 4' 
    },
    'Whispering Forest Part 4': {
        'Story': 'The Dark Rider falls to the ground, bursting into a cloud of dark smoke and vanishing. Once the smoke clears you see a glinting object on the ground. You walk over and pick it up \n( type "pick up" to pick up the object )',
        'North': '',
        'South': '',
        'Pick Up': 'Sacred Relic',
        'Continue': 'Village of Arion Part 3',
        'Image': 'images/whispering_forest_pt4.png',
        'Enemy': None
    },
    'Village of Arion Part 3': {
        'Story': 'You make your way out of the Whispering Forest and return to the Village of Arion, Time to visit the Temple of Ages to find the last Sacred Relic. \n( type "south" to go to the Temple of Ages ).',
        'North': '', 
        'South': 'Temple of Ages Part 1', 
        'Image': 'images/village_of_arion_pt2.png',
        'Enemy': None
    },
    'Village of Arion Part 4': {
        'Story': 'You make your way out of the Temple of Ages and return to the Village of Arion, Time to find Malakars Fortress and put and end to his reign of terror!. \n( End of Demo, More to come in the future! ).',
        'North': '', 
        'South': '', 
        'Image': 'images/village_of_arion_pt2.png',
        'Enemy': None
    },
    'Temple of Ages Part 1': {
        'Story': 'You find yourself in a desert, the barren land with mountainous sand dunes has a mysterious, desolate feel to it. In the distance you see what looks like a temple... \n(type "north" to continue to the Temple or "south" to return to the Village)',
        'North': 'The Village of Arion Part 3',
        'South': 'Temple of Ages Part 2',
        'Image': 'images/temple_of_ages_pt1.png',
        'Enemy': None
    },
    'Temple of Ages Part 2': {
        'Story': 'You approach the front gates of the Temple of Ages, at the foot of one of the pillars you see a bottle half buried in the sand and go over to pick it up \n( type "pick up" to get the Health Elixir)',
        'Pick Up': 'Health Elixir',
        'Continue': 'Temple of Ages Part 3',
        'Image': 'images/temple_of_ages_pt2.png',
        'Enemy': None
    },
    'Temple of Ages Part 3': {
        'Story': 'You walk through the large entrance into the Temple of Ages. As you walk into the great hall, you hear a clattering sound, as your turn to look you see a skeleton like figure walking towards you brandishing weapons! \n( type "fight" to start the battle )',
        'Fight': 'start_fight()',
        'Enemy': 'Boneguard',
        'Continue': 'Temple of Ages Part 4',
        'Image': 'images/temple_of_ages_pt3.png',
    },
    'Temple of Ages Part 4': {
        'Story': 'The Boneguard falls over and crumble into a pile of bones and dust. As the dust settles you see another Sacred Relic glinting between the pile of bones. You walk over and pick it up \n( type "pick up" to pick up the relic)',
        'North': '',
        'South': '',
        'Pick Up': 'Sacred Relic',
        'Continue': 'Village of Arion Part 4',
        'Image': 'images/temple_of_ages_pt4.png',
        'Enemy': None
    }
    
}

"""
Initialize Game Items
"""

health_elixir = Item('Health Elixir', 30)
sacred_relic = Item('Sacred Relic', 1)

"""
Initialize game status at starting point and other components
"""
inventory = Inventory()
status = Status('Village of Arion Part 1', game_places)
parser = CommandParser(inventory, status)


def make_game_window():
    '''Creates the PySimplueGUI game window'''
    sg.theme('Dark Blue 3')

    font_style = ('Arial', 14)

    '''Get the image from the game_state location'''
    story, image = status.get_current_scene()

    left_column = [
        [sg.Image(filename=image, key='-IMG-', size=(650, 650))]
    ]

    right_column = [
        [sg.Text(story, size=(60, 20), key='-OUTPUT-', font=font_style)],
        [sg.Input(key='-IN-', size=(40, 1), font=font_style)],
        [sg.Button('Submit', font=font_style), sg.Button('Exit', font=font_style)]
    ]

    '''Layout for game window'''
    layout = [
        [sg.Column(left_column), sg.Column(right_column)]
    ]

    
    return sg.Window('Legend of the Sacred Forest', layout, size=(1920, 1080), finalize=True)

def main():
    '''Main game loop logic and window creation'''
    window = make_game_window()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Submit':
            user_input = values['-IN-']
            output, image = parser.parse(user_input, game_places)

            '''Update the game output and image'''
            window['-OUTPUT-'].update(output)
            if image:
                window['-IMG-'].update(filename=image)
            
            window['-IN-'].update('')

    window.close()

if __name__ == '__main__':
    main()