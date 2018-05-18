#!/usr/bin/env python3

"""This is the Game Rock, Paper, Scissors

Rock blunts scissors
Paper covers rock
Scissors cut paper

"""

from game import Game
from game import COMPUTER, USER, TIE


class RockPaperScissors(Game):
    """Class for Rock, Paper, Scissors game

    """

    def __init__(self):
        """Constructor for Rock, Paper, Scissors game

        Adds the description, instruction and options
        for the game and calls the base class constructor

        """
        self.description = "\nGame: Rock, Paper, Scissors\n"
        self.instruction = "\nSelect 'r' for Rock, 'p' for Paper, 's' for Scissors"
        self.options = ['r', 'p', 's']
        super(RockPaperScissors, self).__init__(self.options, self.description, self.instruction)

    def decide_winner(self, user_input, computer_input):
        """Decides the winner based on the user input and
        the computer's input

        Rock blunts scissors, Paper covers rock,
        Scissors cut paper

        """
        if user_input == 'p' and computer_input == 'r':
            return USER
        elif user_input == 'r' and computer_input == 's':
            return USER
        elif user_input == 's' and computer_input == 'p':
            return USER
        elif user_input == computer_input:
            return TIE
        return COMPUTER
