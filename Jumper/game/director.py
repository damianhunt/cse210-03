from game.puzzle import Puzzle
from game.parachute import Parachute
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        #self._is_playing = True
        self._parachute = Parachute()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_inputs()
        self._do_updates()
        self._do_outputs()
        while input("Play Again? (Y/N) ").upper() == "Y":
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        #else:
        #    print("Game Over")

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        Puzzle.guess(self)

    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        #self._hider.watch_seeker(self._seeker)
        Parachute.display_parachute(self._parachute)
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        #hint = self._hider.get_hint()
        #self._terminal_service.write_text(hint)
        #if self._hider.is_found():
        #    self._is_playing = False