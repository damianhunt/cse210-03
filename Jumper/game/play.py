from game.puzzle import Puzzle
from game.parachute import Parachute
from game.terminal import TerminalService


class Play:
    def __init__(self):
        self._puzzle = Puzzle()
        self._terminal = TerminalService()

        self._word_completion = "_" * len(self)
        self._guessed = False
        self._guessed_letters = []
        self._guessed_words = []
        self._tries = 6

    def game:
        start_game

    def start_game(self):
        word = self._puzzle.get_word(self)
        Play.play_game(word)
        while input("Play Again? (Y/N) ").upper() == "Y":
            word = self._puzzle.get_word(self)
            Play.play_game(word)
        else:
            print("Game Over")

