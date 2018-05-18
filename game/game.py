#!/usr/bin/env python3

"""This is the Game base class

This can be used as a base class for
any type of games like rock, paper, scissors
"""

import sys
import random

COMPUTER = 'Computer'
USER = 'You'
TIE = 'Game Tied'


class Game(object):
    """Base class for Game

    """

    def __init__(self, options, description, instruction):
        """Constructor for the base class

        Initializes the basic variables and prints
        the description of the game at the start
        of the game.

        """
        self.options = options
        self.description = description
        self.instruction = instruction + ", 'e' for exit\n"
        print(self.description)

    def get_input_from_computer(self):
        """Generates random input from options.

        Generates random input from options
        and returns the randomly generates
        option.

        """
        return random.choice(self.options)

    def validate_input(self, user_input):
        """Validates the user given input

        Makes sure user given input is part
        of the options list or a call to
        exit the game

        """
        if user_input == 'e':
            sys.exit()
        elif user_input not in self.options:
            raise Exception("Invalid input: %s, Valid inputs: %s"\
                            % (user_input, self.options))

    def play_game(self):
        """Logic for playing the game.

        Gets input from the user, validates it and
        calculates the winner and prints it.

        """
        while True:
            user_input = input(self.instruction)
            try:
                self.validate_input(user_input)
            except Exception as exp:
                print(exp)
                continue
            computer_input = self.get_input_from_computer()
            winner = self.decide_winner(user_input, computer_input)
            print("Computer played: %s" % computer_input)
            if winner == USER:
                print("%s won!!" % USER)
            elif winner == COMPUTER:
                print("%s lost!!" % USER)
            else:
                print(TIE)

    def decide_winner(self, user_input, computer_input):
        """Abstract method for having the logic
        for decising the winner.

        """
        # implement the logic in child class
        raise NotImplementedError
