
class Parachute:
    
    def __init__(self):
        self._tries = 5
        self._stages = [  # final state: Parachute completely gone, player dies
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

    def display_parachute(self, tries):
        
        return self._stages[tries]
