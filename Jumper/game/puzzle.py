from random import Random
from game.parachute import Parachute


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
                    'chill', 'seed', 'born', 'shampoo', 'italian', 'giggle', 'roost', 'palm',
                    'globe', 'wise', 'grandson', 'running', 'sunlight', 'spending', 'crunch',
                    'tangle', 'forego', 'tailor', 'divinity', 'probe', 'bearded', 'premium',
                    'featured', 'serve', 'borrower', 'examine', 'legal', 'outlive', 'unnamed',
                    'unending', 'snow', 'whisper', 'bundle', 'bracket', 'deny', 'blurred', 'pentagon',
                    'reformed', 'polarity', 'jumping', 'gain', 'laundry', 'hobble', 'culture',
                    'whittle', 'docket', 'mayhem', 'build', 'peel', 'board', 'keen', 'glorious',
                    'singular', 'cavalry', 'present', 'cold', 'hook', 'salted', 'just', 'dumpling',
                    'glimmer', 'drowning', 'admiral', 'sketch', 'subject', 'upright', 'sunshine',
                    'slide', 'calamity', 'gurney', 'adult', 'adore', 'weld', 'masking', 'print',
                    'wishful', 'foyer', 'tofu', 'machete', 'diced', 'behemoth', 'rout', 'midwife',
                    'neglect', 'mass', 'game', 'stocking', 'folly', 'action', 'bubbling',
                    'scented', 'sprinter', 'bingo', 'egyptian', 'comedy', 'rung', 'outdated',
                    'radical', 'escalate', 'mutter', 'desert', 'memento', 'kayak', 'talon',
                    'portion', 'affirm', 'dashing', 'fare', 'battle', 'pupil', 'rite',
                    'smash', 'true', 'entrance', 'counting', 'peruse', 'dioxide', 'hermit',
                    'carving', 'backyard', 'homeless', 'medley', 'packet', 'tickle',
                    'coming', 'leave', 'swing', 'thicket', 'reserve', 'murder', 'costly',
                    'corduroy', 'bump', 'oncology', 'swatch', 'rundown', 'steal', 'teller',
                    'cable', 'oily', 'official', 'abyss', 'schism', 'failing', 'guru',
                    'trim', 'alfalfa', 'doubt', 'booming', 'bruised', 'playful', 'kicker',
                    'jockey', 'handmade', 'landfall', 'rhythm', 'keep', 'reassure', 'garland',
                    'sauna', 'idiom', 'fluent', 'lope', 'gland', 'amend', 'fashion', 'treaty',
                    'standing', 'current', 'sharpen', 'cinder', 'idealist', 'festive', 'frame',
                    'molten', 'sill', 'glisten', 'fearful', 'basement', 'minutia', 'coin',
                    'stick', 'featured', 'soot', 'static', 'crazed', 'upset', 'robotics',
                    'dwarf', 'shield', 'butler', 'stitch', 'stub', 'sabotage', 'parlor',
                    'prompt', 'heady', 'horn', 'bygone', 'rework', 'painful', 'composer',
                    'glance', 'acquit', 'eagle', 'solvent', 'backbone', 'smart', 'atlas',
                    'leap', 'danger', 'bruise', 'seminar', 'tinge', 'trip', 'narrow',
                    'while', 'jaguar', 'seminary', 'command', 'cassette', 'draw', 'anchovy',
                    'scream', 'blush', 'organic', 'applause', 'parallel', 'trolley', 'pathos',
                    'origin', 'hang', 'pungent', 'angular', 'stubble', 'painted', 'forward',
                    'saddle', 'muddy', 'orchid', 'prudence', 'disprove', 'yiddish', 'lobbying',
                    'neuron', 'tumor', 'haitian', 'swift', 'mantel', 'wardrobe', 'consist',
                    'storied','extreme','payback','control','dummy','influx','realtor', 'detach',
                    'flake','consign','adjunct','stylized','weep','prepare','pioneer','tail',
                    'platoon','exercise','dummy','clap','actor','spark','dope','phrase','welsh',
                    'wall','whine','fickle','wrong','stamina','dazed','cramp','filet','foresee','seller',
                    'award','mare','uncover','drowning','ease','buttery','luxury','bigotry','muddy','photon','snow',
                    'oppress','blessed','call','stain','amber','rental','nominee','township','adhesive','lengthy',
                    'swarm','court','baguette','leper','vital','push','digger','setback','accused','taker','genie',
                    'reverse','fake','widowed','renewed','goodness','featured','curse','shocked','shove',
                    'marked','interact','mane','hawk','kidnap','noble','proton','effort','patriot','showcase',
                    'parish','mosaic','coil','aide','breeder','concoct','pathway','hearing','bayou','regimen','drain',
                    'bereft','matte','bill','medal','prickly','sarcasm','stuffy','allege','monopoly',
                    'lighter','repair','worship','vent','hybrid','buffet','lively'
                    ]
        #self._get_word = Random.choice(self._list)
        self._guessed_letters = []
        self.guessed_words = []

    def get_word(self):
        word = Random.choice(self._list)
        return word.upper()

    def guess(self):
        while not guessed and Parachute.self._parachute > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in self._guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in self._get_word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    self._guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    self._guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(Puzzle.get_word(self)) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(Puzzle.get_word(self)) and guess.isalpha():
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)
                elif guess != Puzzle.get_word(self):
                    print(guess, "is not the word.")
                    tries -= 1
                    self.guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = Puzzle.get_word(self)
            else:
                print("Not a valid guess.")
            print(Parachute.display_parachute(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " + Puzzle.get_word(self) + ". Maybe next time!")
