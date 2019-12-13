import pytest

from day_1 import *

def test_calculate_required_fuel_for_module():
    mass = 12

    fuel = calculate_required_fuel_for_module(mass)

    assert fuel == 2

def test_get_fuel_with_no_mass():
    masses = []

    fuel = get_fuel_required(masses)

    assert fuel == 0

def test_get_fuel_with_one_mass():
    masses = [12]

    fuel = get_fuel_required(masses)

    assert fuel == 2

def test_get_fuel_with_multiple_masses():
    masses = [12,12]

    fuel = get_fuel_required(masses)

    assert fuel == 4

def test_solution_part_a():
    assert get_fuel_required_solution_part_a() == 3212842
