
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
    
        