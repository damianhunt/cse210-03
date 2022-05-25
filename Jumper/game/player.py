from Jumper.game.word import Word
from parachute import Parachute
from terminal_service import TerminalService

class Game:
    '''
    The Director of the Game.
    
    Responsibility: Control the sequence/flow of Gameplay.
    
    Attributes:
        game_in_progress (Boolean):
            Whether or not the game is
            currently being played or not.
        Word:
            The word generator for the parachute game.
        
    '''
    
    def __init__(self):
        
        self._parachute = Parachute()
        self._game_in_progress = True
        self._guesses = False
        self._word = Word()
        self._terminal_service = TerminalService()
       
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._game_in_progress:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_number("\nGuess a letter: ")
        self._seeker.move_location(new_location)