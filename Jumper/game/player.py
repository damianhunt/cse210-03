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
        
        self._game_in_progress = True
        self._guesses = False
        self._complete_word = '_' * len(Puzzle.get_word())
        self._guessed_letters = []
        self._words = []
        self._tries = 6
       