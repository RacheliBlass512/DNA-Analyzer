from Commands.Command import Command
from Commands.helper_functions_command import get_dna_by_id, get_good_name, get_seq_to_print, not_valid_str
from DNA.DNA import DNA


class DupCommand(Command):

    def execute(self, *args):
        if len(args) == 2 and args[1][0] == '@' and args[0][0] == '#':
            the_dna = get_dna_by_id(args[0][1:])
            original_name = args[1][1:]
        elif len(args) == 1 and args[0][0] == '#':
            the_dna = get_dna_by_id(args[0][1:])
            if not the_dna:
                return 'not exist this ID'
            original_name = the_dna.get_name()
        else:
            return not_valid_str
        new_name = get_good_name(original_name)
        new_dna = DNA(the_dna.get_sequence() + the_dna.get_sequence(), new_name)
        Command.dna_array.append(new_dna)
        return f'[{new_dna.get_id()}] {new_dna.get_name()}: {get_seq_to_print(new_dna.get_sequence())}'
