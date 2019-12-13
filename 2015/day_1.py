from common import read_characters

def get_floor(directions):
    floor = 0
    for direction in directions:
        if direction == '(':
            floor += 1
        elif direction == ')':
            floor -= 1

    return floor

def get_floor_solution():
    return  get_floor(read_characters('2015/input/input1.txt'))

if __name__ == '__main__':
    print("TODO")
