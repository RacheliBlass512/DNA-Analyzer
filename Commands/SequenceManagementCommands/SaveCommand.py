from Commands.Command import Command
from Commands.helper_functions_command import get_dna, not_valid_str


class SaveCommand(Command):
    def execute(self, *args):
        dna = get_dna(args[0])
        if not dna:
            return 'not valid Id / name'
        if len(args) == 2:
            file_name = args[1]
        elif len(args) == 1:
            file_name = dna.get_name() + '.rawdna'
        else:
            return not_valid_str
        with open(file_name, 'w') as file:
            file.write(dna.get_sequence().get_string())
        return 'the sequence saved successfully'
