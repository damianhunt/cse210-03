from play import Play
from puzzle import Puzzle
from parachute import Parachute

class Director:
    
    def start_game():
        word = Puzzle.get_word()
        Play.play_game(word)
        while input("Play Again? (Y/N) ").upper() == "Y":
            word = Puzzle.get_word()
            Play.play_game(word)
        else:
            print("Game Over")
