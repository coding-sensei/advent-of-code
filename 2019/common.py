def read_characters(filename):
    return convert_file(filename, str)

def read_numbers(filename):
    return convert_file(filename, int)

def convert_file(filename, convert):
    with open(filename) as f:
        return [convert(x.strip()) for x in f.readlines()]
