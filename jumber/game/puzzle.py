import random
from re import M

class Puzzle:
   """
      The puzzle that should be guessed
      The responsibility of the puzzle is to contain words that should be gussed. 
      It also checks status of the guess and updates the puzzle
      
      Atributes:
      Args:
         self (puzzle): A instance of the Puzzle.
         secret word : A word the player should guess
         letters: The characters a player should use to guess the words 
   """
    

   def __init__(self):
      """
      construct a new Puzzle
      
      Args
         self(Puzzle): An instance of the Puzzle
      """
      self.words = ['mum', 'dad', 'sister', 'brother', 'me', 'you', 'mine', 
                    'ours', 'mother', 'father', 'aunt','grandma',"walk","wall","wander",
                    "want","war","warm","warn","wary","wash","waste",
                    "yam","yard","yarn","yawn","year","yell","yellow",
                    "fact","fade","faded","fail","faint","fair",
                    "class","clean","clear","clever","clip",
                    "close","closed","cloth",
                    "cloudy","clover","club","afford","afraid",]
      self.secret_word = random.choice(self.words)
      self.letters = ['_' for char in self.secret_word] 
      self.user_input = ''
   
   def draw_puzzle(self):
      """
      Update the status of the puzzle.
      
       Args:
              self (puzzle): A instance of the Puzzle.
      """
      print(self.letters)
       
 
    
   def prompt_for_aguess(self):
      """
      input from the player.
      
      Args:
              self (puzzle): A instance of the Puzzle.
              
      returns
            A character entered by the player.
      """
      self.user_input = input('What is the next letter?  ')
   
    
   def check_guess(self):
      """
      Takes the character by the user compare it with the characters in the 
      secret word.

      Args:
              self (puzzle): A instance of the Puzzle.
              user input: Character entered by the player
              secret word: the word the player is guessing
              
      returns
            A boolean : result of the comparison
      """
       
      if self.user_input in self.secret_word:
          #Update letters
         for index, letter in enumerate(self.secret_word):
            if letter == self.user_input:
               self.letters[index] = self.user_input
          #Confirmation Message
         print('You gessed correctly. ')
         return True
      else:
          #Print is not correct
          print('Wrong Letter. Try again. ')
          return False
          
   def puzzle_complete(self):
      """
      Checks to if all the characters in the secret word has been guessed.
      
      Args
            self(Puzzle): An instance of the Puzzle.
            letters: Characters in each word
            
      returns
            A boolean: A result of the comparison between the number of 
            characters in the word and the chances given to guess.
      """
      for char in self.letters:
         if char == "_":
            return False
      return True