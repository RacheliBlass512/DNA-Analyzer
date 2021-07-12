from Commands.BatchCommands.BatchCommand import BatchCommand


class RunningBatches(BatchCommand):
    def execute(self, *args):
        if not len(args) == 1 and args[0][0] == '@':
            return 'expected batch name with \'@\' prefix after the command "run"'
        all_commands = self.batches_dict.get(args[0][1:])
        if all_commands is None:
            return 'not exists this batch name'
        for cmd in all_commands:
