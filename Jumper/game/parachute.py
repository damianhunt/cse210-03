
class parachute:


    def display_parachute(tries):
        stages = [  # final state: Parachute completely gone, player dies
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
        return stages[tries]
