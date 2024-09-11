'''Status Module'''

class Status:
    def __init__(self, initial_state, game_places):
        '''Initialize with the starting game state and game places'''
        self.game_state = initial_state
        self.game_places = game_places

    def get_current_scene(self):
        '''Return the current scene's story and image based on game_state'''
        current_place = self.game_places[self.game_state]
        return current_place['Story'], current_place['Image']
    
    def update_state(self, action):
        '''Update the game state based on user action and return the updated scene'''
        current_place = self.game_places[self.game_state]

        '''Handle movement and actions'''
        if action in current_place:
            self.game_state = current_place[action]
        else:
            return "Invalid Action", None
        return self.get_current_scene()
    
    def get_state(self):
        '''Return current game state'''
        return self.game_state
