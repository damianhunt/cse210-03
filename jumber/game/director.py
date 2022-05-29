from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.parachute import Parachute


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
    parachute(Parachute()): The parachute in the game
    puzzle(Puzzle()): The Puzzle in the game
    terminal_services(Terminal Services()): Reads and displays information to the user

        
    """

    def __init__(self):
       """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
       """
       self._puzzle = Puzzle()
       self._parachute = Parachute()
       self._terminal_services = TerminalService()
   
   
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self._write_instructions()
        
        while self.is_game_over() == False:
            self._puzzle.draw_puzzle()
            self._parachute.draw_parachute()
            self._puzzle.prompt_for_aguess()
            guess_result = self._puzzle.check_guess()
            self._parachute.update_parachute(guess_result)
            
            
        if self._parachute.parachute_alive:
            #Print messfor
            print('You won!!!!')
            print('The word was ' + self._puzzle.secret_word)  
            
        else:
            self._parachute.draw_parachute()
            print('The word was ' + self._puzzle.secret_word)
            print('Game Over!!. Try again next time.')
        
    
    def _write_instructions(self):
        """
        Displays instructions of the game to the player.
        
        Args:
           self (Director): an instance of Director.
        """
        print(' Jumber is a guessing game. Choose any letter from a to z to build')
        print('a word from the word bank. See how many words you can build.') 
        print('Are you ready for the challenge ?')
    
    def is_game_over(self):
        """
        Checks if the player has attempts to play the game or it is game over.
         Args:
            self (Director): an instance of Director.
        """
        if self._parachute.parachute_alive and not self._puzzle.puzzle_complete():
            return False
        else:
            return True
        
