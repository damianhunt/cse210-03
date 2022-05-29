class Parachute:
    """
    A class that handles play attempts for each player.
    
    Attributes:
        parachute: the chances of playing before game is over
        parachute alive: A state of the parachute
    
    """

    def __init__(self):
        """
        Construct a new parachute
        Args
            self(Parachute)   An instance of the  Parachute
        """
        
        
        self.new_parachute = [' ___', '/___\\', '\\   /', ' \\ /', '  0', ' /|\\',' / \\', '^^^^^']
        self.parachute_alive = True
   
    def draw_parachute(self):
        """Draws a new parachute
        
          Args:
                self(Parachute): An instance of the Parachute    
        """
        for line in self.new_parachute:
            print(line)
          
    def update_parachute(self, status):
        """
        Checks the status of the guess to update the status of the parachute
        
        Args:
        self (update_parachute) an instance of the update_parachute.
        status (a boolean) from the check_quess. 
        """
        if status == True:
            return
        else:
          self.new_parachute.pop(0)
          if len(self.new_parachute) == 4:
              self.parachute_alive = False
              self.new_parachute[0] = '  x'

              
          
    