

class Parachute:
    def __init__(self, attempts):
       
       self._parachute = attempts
       
    def draw_parachute(attempts):
        parachute = [
            '''
             ___
            /___\\
            \   /
             \ /
              0
             /|\\
             / \\
            '''
            ,
            '''
            /___\\
            \   /
             \ /
              0
             /|\\
             / \\
            '''
            ,
            '''
            \   /
             \ /
              0
             /|\\
             / \\
            '''
            ,
            '''
             \ /
              0
             /|\\
             / \\
            '''
            ,
            '''
              x
             /|\\
             / \\
            '''
        ]
        return parachute[attempts]
        