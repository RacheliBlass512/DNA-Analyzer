from Commands.Command import Command
from Commands.helper_functions_command import not_valid_str, get_good_name, get_seq_to_print
from DNA.DNA import DNA


class NewCommand(Command):
    def execute(self, *args):
        if len(args) == 2 and args[1][0] == '@':
            original_name = args[1][1:]
        elif len(args) == 1:
            original_name = 'seq_1'
        else:
            return not_valid_str
        new_name = get_good_name(original_name)
        new_dna = DNA(args[0], new_name)
        Command.dna_array.append(new_dna)
        return f'[{new_dna.get_id()}] {new_dna.get_name()}: {get_seq_to_print(new_dna.get_sequence())}'
