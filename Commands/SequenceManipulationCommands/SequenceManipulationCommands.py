from Commands.Command import Command
from Commands.helper_functions_command import not_valid_str, get_dna, get_good_name
from DNA.DNA import DNA


class SequenceManipulationCommands(Command):
    def execute(self, *args):
        try:
            command = args
            if len(command) < 3:
                return not_valid_str
            dna = get_dna(command[0])
            sequence = dna.get_sequence()
            new_sequence = self.manipulate(command, sequence)
            if command[-2] == ':':
                new_name = None
                if command[-1] == '@@':
                    new_name = dna.get_name() + self.suffix
                elif command[-1][0] == '@':
                    new_name = command[-1][1:]
                dna = DNA(new_sequence, get_good_name(new_name))
                Command.dna_array.append(dna)
            else:
                dna.set_sequence(new_sequence)
            return f'[{dna.get_id()}] {dna.get_name()}: {dna.get_sequence()}'
        except (IndexError, ValueError, TypeError):
            return not_valid_str

    def manipulate(self, command, sequence):
        pass
