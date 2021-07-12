from Commands.Command import Command
from Commands.helper_functions_command import not_valid_str, get_dna


class FindCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            return not_valid_str
        if get_dna(args[0]):
            big_sequence = get_dna(args[0]).get_sequence().get_string()
        else:
            return not_valid_str
        if get_dna(args[1]):
            sub_sequence = get_dna(args[1]).get_sequence().get_string()
        else:
            sub_sequence = args[1]
        return self.handle_find(big_sequence, sub_sequence)

    def handle_find(self, big_sequence, sub_sequence):
        pass
