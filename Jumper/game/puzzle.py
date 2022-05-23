from random import Random


class Puzzle:

    def __init__(self):
        self._list = ["animals", "country", "remotes", 'wares', 'soup', 'mount', 'extend',
                    'brown', 'expert', 'tired', 'humidity', 'backpack', 'crust', 'dent', 
                    'market', 'knock', 'smite', 'windy', 'coin', 'throw','silence', 'bluff', 
                    'downfall', 'climb', 'lying', 'weaver', 'snob', 'kickoff', 'match', 'quaker',
                    'foreman', 'excite', 'thinking', 'mend', 'allergen', 'pruning', 'coat',
                    'emerald', 'coherent', 'manic', 'multiple', 'square','funded', 'funnel',
                    'sailing', 'dream', 'mutation', 'strict', 'mystic', 'film', 'guide',
                    'strain', 'bishop', 'settle', 'plateau', 'emigrate', 'marching', 'optimal',
                    'medley', 'endanger', 'wick', 'condone', 'schema', 'rage', 'figure',
                    'plague', 'aloof', 'there', 'reusable', 'refinery', 'suffer', 'affirm',
                    'captive', 'flipping', 'prolong', 'main', 'coral', 'dinner', 'rabbit',
                    'chill', 'seed',
                    ]

    def get_word(self):
        random_word = Random.choice(self._list)
        return random_word.upper()