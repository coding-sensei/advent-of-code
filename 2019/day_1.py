from common import read_numbers

def calculate_required_fuel_for_module(mass):
    return (int(mass/3) - 2)

def get_fuel_required(list_of_masses):
    return sum([calculate_required_fuel_for_module(mass) for mass in list_of_masses])

def get_fuel_required_solution_part_a():
    return  get_fuel_required(read_numbers('2019/input/input1.txt'))

if __name__ == '__main__':
    print("TODO")
