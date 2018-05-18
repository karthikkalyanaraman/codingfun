# tests.py

"""Unit tests for game.py and rock_paper_scissors.py

"""

import pytest
import mock
from game import Game
from game import COMPUTER, USER, TIE
from rock_paper_scissors import RockPaperScissors
from mock_true import MockTrue


@pytest.fixture
def basic_game():
    """Returns a basic Game instance.

    """
    return Game(['a', 'b', 'c'], "description", "instructions")


def test_basic_game_constructor(basic_game):
    """Tests the constructor.

    """
    assert basic_game.description == "description"
    assert basic_game.instruction == "instructions, 'e' for exit\n"
    assert basic_game.options == ['a', 'b', 'c']


def test_get_input_from_computer(basic_game):
    """Tests __get_input_from_computer.

    """
    assert basic_game.get_input_from_computer() in ['a', 'b', 'c']


def test_validate_bad_input(basic_game):
    """Tests validate_input.

    """
    with pytest.raises(Exception) as e_info:
        basic_game.validate_input('q')


@pytest.mark.xfail
def test_validate_good_input(basic_game):
    """Tests validate_input.

    """
    with pytest.raises(Exception) as e_info:
        basic_game.validate_input('a')


def test_validate_exit(basic_game):
    """Tests the exit option

    """
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        basic_game.validate_input('e')
    assert pytest_wrapped_e.type == SystemExit


@pytest.fixture
def rock_paper_scissors_game():
    """Returns a RockPaperScissors instance.

    """
    return RockPaperScissors()


def test_play_game(monkeypatch, rock_paper_scissors_game):
    """Tests the play_game.

    """
    monkeypatch.setattr('builtins.input', lambda x: 'r')
    with mock.patch('__builtin__.True', MockTrue(0)):
        rock_paper_scissors_game.play_game()


def test_decide_winner(rock_paper_scissors_game):
    """Tests the decide_winner.

    """
    assert rock_paper_scissors_game.decide_winner('p', 'r') == USER
    assert rock_paper_scissors_game.decide_winner('r', 's') == USER
    assert rock_paper_scissors_game.decide_winner('s', 'p') == USER
    assert rock_paper_scissors_game.decide_winner('s', 's') == TIE
    assert rock_paper_scissors_game.decide_winner('r', 'p') == COMPUTER
    assert rock_paper_scissors_game.decide_winner('s', 'r') == COMPUTER
    assert rock_paper_scissors_game.decide_winner('p', 's') == COMPUTER
