from Commands.SequenceManipulationCommands.SequenceManipulationCommands import SequenceManipulationCommands
from DNA.DnaSequence import DnaSequence


class ReplaceCommand(SequenceManipulationCommands):
    def __init__(self):
        self.suffix = '_r1'

    def execute(self, *args):
        return super().execute(*args)

    def manipulate(self, command, sequence):
        slices_limits = len(command) - 2 if command[-2] == ':' else len(command)
        new_sequence = sequence.get_string()
        try:
            for i in range(1, slices_limits, 2):
                new_sequence = new_sequence[:int(command[i])] + command[i + 1] + new_sequence[int(command[i]) + 1:]
            return new_sequence
        except IndexError:
            return None
