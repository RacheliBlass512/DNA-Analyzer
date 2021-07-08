from DNA import DNA

not_valid_str = "not valid command"
missing_char = "expected @"


class Command:
    dna_array = []

    def execute(self, *args):
        pass

    # def handle_syntax(self, command):
    #     parts = command.split()
    #     if parts[0] in ['']
    #     print(parts)


def get_dna_by_id(id):
    for dna in Command.dna_array:
        if str(dna.get_id()) == id:
            return dna
    return None


class NewCommand(Command):
    def execute(self, *args):
        if len(args) == 2 and args[1][0] == '@':
            original_name = args[1][1:]
        # elif len(args) == 2 and args[1][0] == '#':
        #     original_name = get_name_by_id(args[1][1:])
        elif len(args) == 1:
            original_name = 'seq_1'
        else:
            return not_valid_str
        new_name = get_good_name(original_name)
        new_dna = DNA(args[0], new_name)
        Command.dna_array.append(new_dna)
        return f'[{new_dna.get_id()}] {new_dna.get_name()}: {get_seq_to_print(new_dna.get_sequence())}'


class LoadCommand(Command):
    def execute(self, *args):
        file_name = args[0]
        if len(args) == 2 and args[1][0] == '@':
            original_name = args[1][1:]
        # elif len(args) == 2 and args[1][0] == '#':
        #     original_name = get_name_by_id(args[1][1:])
        elif len(args) == 1:
            original_name = file_name.split('.')[0]
        else:
            return not_valid_str
        # if len(args) != 1 and len(args) != 2:
        #     return not_valid_str
        # if len(args) == 2 and args[1][0] not in '@#':
        #     return missing_char
        # if len(args) == 1:
        #     seq_name = get_good_name()
        # else:
        #     seq_name = get_good_name(args[1][1:])
        seq_name = get_good_name(original_name)
        try:
            f = open(file_name)
            sequence = f.readline()
        except FileNotFoundError:
            return 'file not found, try another'
        new_dna = DNA(sequence, seq_name)
        Command.dna_array.append(new_dna)
        return f'[{new_dna.get_id()}] {new_dna.get_name()}: {get_seq_to_print(sequence)}'


class DupCommand(Command):
    def execute(self, *args):
        if len(args) == 2 and args[1][0] == '@' and args[0][0] == '#':
            the_dna = get_dna_by_id(args[0][1:])
            original_name = args[1][1:]
        elif len(args) == 1 and args[0][0] == '#' :
            the_dna = get_dna_by_id(args[0][1:])
            if not the_dna:
                return 'not exist this ID'
            original_name = the_dna.get_name()
        else:
            return not_valid_str
        new_name = get_good_name(original_name)
        new_dna = DNA(the_dna.get_sequence()+the_dna.get_sequence(), new_name)
        Command.dna_array.append(new_dna)
        return f'[{new_dna.get_id()}] {new_dna.get_name()}: {get_seq_to_print(new_dna.get_sequence())}'


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
