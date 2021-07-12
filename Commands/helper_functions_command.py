from Commands.Command import Command

not_valid_str = "command invalid"
missing_char = "expected @"


def get_dna_by_id(my_id):
    for dna in Command.dna_array:
        if str(dna.get_id()) == my_id:
            return dna
    return None


def get_dna_by_name(my_name):
    for dna in Command.dna_array:
        if dna.get_name() == my_name:
            return dna
    return None


def get_good_name(expected_name):
    for dna in Command.dna_array:
        if dna.get_name() == expected_name:
            if expected_name[-1].isnumeric():
                return get_good_name(expected_name[:-1] + str(int(expected_name[-1]) + 1))
            return get_good_name(expected_name + '_1')
    return expected_name


def get_seq_to_print(sequence):
    if len(sequence) > 40:
        return sequence[:32] + '...' + sequence[-3:]
    return sequence


def get_dna(string):
    if string[0] == '#':
        return get_dna_by_id(string[1:])
    elif string[0] == '@':
        return get_dna_by_name(string[1:])
    return None
