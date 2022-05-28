from game.word import Word
from game.parachute import Parachute
from game.terminal_service import TerminalService

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
        self._guessed_letters = []
        self.word_completion = "_" * len(self._word)
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
        letter = self._terminal_service.read_text("\nGuess a letter: ")
        
        
    def _do_updates(self):
        # What needs to be updated?
        # Number of tries if the guessed letter is wrong
        # Word completion if the letter guessed is the right one.
        pass
        
    def _do_outputs(self):
        # What to display?
        # Display the stage of the parachute depending on how many tries user has left.
        # Word Completion.
        self._terminal_service.write_text(self._parachute.display_parachute(5))
        