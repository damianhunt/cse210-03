
class Parachute:
    def __init__(self):
   
        self._parachute = [  # final state: Parachute completely gone, player dies
                    """
                     x
                    /|\\
                    / \\
                    
                  ^^^^^^^  
                    """,
                    # another piece gone
                    """
                    \\/
                     o
                    /|\\
                    / \\
                    
                  ^^^^^^^  
                    """,
                    # another piece gone
                    """
                   \\  /
                    \\/
                     o
                    /|\\
                    / \\
                    
                  ^^^^^^^  
                    """,
                    # another piece gone
                    """
                    ___
                   \\  /
                    \\/
                     o
                    /|\\
                    / \\
                    
                  ^^^^^^^  
                    """,
                    # one piece off parachute
                    """
                   /___\\
                   \\  /
                    \\/
                     o
                    /|\\
                    / \\
                    
                  ^^^^^^^  
                    """,
                    # initial parachute state
                    """
                    ___
                   /___\\
                   \\  /
                    \\/
                     o
                    /|\\
                    / \\
                    
                  ^^^^^^^  
                    """
        ]


    def display_parachute(self,tries):
        stages = self._parachute
        
        return stages[tries]
