from Jumper.game.word import Word
from word import Puzzle
from parachute import Parachute

class Game:
    '''
    The Director of the Game.
    
    Responsibility: Control the sequence/flow of Gameplay.
    
    Attributes:
        game_in_progress (Boolean):
            Whether or not the game is
            currently being played or not.
        Puzzle:
            The word generator for the parachute game.
        
    '''
    
    def __init__(self):
        
        self._parachute = Parachute()
        self._game_in_progress = True
        self._guesses = False
        self._word = Word()
       
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._game_in_progress:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()