from Commands.SequenceAnalysisCommands.FindCommand import FindCommand


class RegularFindCommand(FindCommand):
    def execute(self, *args):
        return super().execute(*args)

    def handle_find(self, big_sequence, sub_sequence):
        return big_sequence.find(sub_sequence)
