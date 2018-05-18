#!/usr/bin/env python3

"""Module to define all custom Exceptions

"""

class InvalidInputException(Exception):
	"""Exception to use for validating
	invalid inputs

	"""
    def __init__(self, error):
        self.error = error
