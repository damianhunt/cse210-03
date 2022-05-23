from random import Random, random


import random

class Puzzle:

    def __init__(self):
        self._list = ["animals, country, remotes, "]

    def word(self):
        list = self._list
        random_word = Random.choice(list)
        return random_word

class Account:

    def __init__(self):
        self._transactions = [] # the "_" prefix means treat this as private
        
    def deposit(self, amount):
        self._transactions.append(amount)