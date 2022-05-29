import random
from re import M

class Puzzle:
   """
      The puzzle that should be guessed
      The responsibility of the puzzle is to contain words that should be gussed. 
      It also checks status of the guess and updates the puzzle
      
      Atributes:
      
   """
    

   def __init__(self):
      """
      Construct a new puzzle
      
      Args:
         self (puzzle)  
      """
      self.words = ['mum', 'dad', 'sister', 'brother', 'me', 'you', 'mine', 'ours', 'mother', 'father', 'aunt','grandma']
      self.secret_word = random.choice(self.words)
      self.letters = ['_' for char in self.secret_word] 
      self.user_input = ''
   
   def draw_puzzle(self):
       print(self.letters)
       
 
    
   def prompt_for_aguess(self):
       self.user_input = input('What is the next letter?  ')
   
    
   def check_guess(self):
       
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
      
      """
      for char in self.letters:
         if char == "_":
            return False
      return True