from CLI.Confirm import Confirm
from Commands.Command import Command
from Commands.helper_functions_command import get_dna


class DelCommand(Command):

    def execute(self, *args):
        dna = get_dna(args[0])
        if not dna:
            return 'not valid Id / name'
        print(f'Do you really want to delete {dna.get_name()}: {dna.get_sequence()}? '
              f'Please confirm by \'y\' or \'Y\', or cancel by \'n\' or \'N\'.')
        confirm = Confirm()
        confirm.start()
        if confirm.get_is_ok():
            Command.dna_array.remove(dna)
            return f'Deleted: [{dna.get_id()}] {dna.get_name()}: {dna.get_sequence()}'
        else:
            return 'The deletion was canceled'
