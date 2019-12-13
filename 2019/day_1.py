from common import read_numbers

def get_fuel_required(list_of_masses):
    total_fuel = 0

    for mass in list_of_masses:
        total_fuel = total_fuel + (int(mass/3) - 2)

    return total_fuel

def get_fuel_required_solution():
    return  get_fuel_required(read_numbers('2019/input/input1.txt'))

if __name__ == '__main__':
    print("TODO")
