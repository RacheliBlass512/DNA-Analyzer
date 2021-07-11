from Commands.Command import Command
from Commands.helper_functions_command import not_valid_str, get_good_name, get_seq_to_print
from DNA.DNA import DNA


class LoadCommand(Command):
    def execute(self, *args):
        file_name = args[0]
        if len(args) == 2 and args[1][0] == '@':
            original_name = args[1][1:]
        elif len(args) == 1:
            original_name = file_name.split('.')[0]
        else:
            return not_valid_str
        seq_name = get_good_name(original_name)
        try:
            f = open(file_name)
            sequence = f.readline()
        except FileNotFoundError:
            return 'file not found, try another'
        new_dna = DNA(sequence, seq_name)
        Command.dna_array.append(new_dna)
        return f'[{new_dna.get_id()}] {new_dna.get_name()}: {get_seq_to_print(sequence)}'
