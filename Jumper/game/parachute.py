
class Parachute:
    def __init__(self, attempts):
       
       self._parachute = attempts
       
    def draw_parachute(attempts):
        parachute = [
            '''
              x
             /|\\
             / \\
                 
           ^^^^^^^
            '''
            ,
            '''
             \ /
              0
             /|\\
             / \\
                 
           ^^^^^^^
            '''
            ,
            '''
            \   /
             \ /
              0
             /|\\
             / \\
                 
           ^^^^^^^
            '''
            ,
            '''
            /___\\
            \   /
             \ /
              0
             /|\\
             / \\
                 
           ^^^^^^^
            '''
            ,
            '''
             ___
            /___\\
            \   /
             \ /
              0
             /|\\
             / \\
                 
           ^^^^^^^
            '''
        ]
        return parachute[attempts]
        

    def play_game(word):
        print("Let's play Jumper!")
        print(Parachute.display_parachute(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in Play.self._guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    Play.self._guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    Play.self._guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in Play.self._guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    Play.self._guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(Parachute.display_parachute(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
