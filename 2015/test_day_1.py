import pytest

from day_1 import get_floor, get_floor_solution

def test_get_floor_with_no_directions():
    directions = []

    floor = get_floor(directions)

    assert floor == 0

def test_get_floor_with_up_direction():
    directions = ['(']

    floor = get_floor(directions)

    assert floor == 1

def test_get_floor_with_down_direction():
    directions = [')']

    floor = get_floor(directions)

    assert floor == -1

def test_get_floor_with_up_and_down_direction():
    directions = [')', '(']

    floor = get_floor(directions)

    assert floor == 0

def test_get_floor_with_multiple_up_and_down_directions():
    directions = [')',')','(','(','(','(','(']

    floor = get_floor(directions)

    assert floor == 3

def test_get_floor_with_input_file():
    directions = [')',')','(','(','(','(','(']

    floor = get_floor(directions)

    assert floor == 3

def test_solution():
    assert get_floor_solution() == 138
