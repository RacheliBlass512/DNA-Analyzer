from Commands.SequenceAnalysisCommands.FindCommand import FindCommand


class findallCommand(FindCommand):
    def execute(self, *args):
        return super().execute(*args)

    def handle_find(self, big_sequence, sub_sequence):
        start_indexes = [i for i in range(len(big_sequence)) if big_sequence.startswith(sub_sequence, i)]
        start_indexes_in_str = [str(i) for i in start_indexes]
        return ' '.join(start_indexes_in_str)
