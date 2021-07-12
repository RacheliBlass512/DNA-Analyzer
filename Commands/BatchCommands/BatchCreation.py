from CLI.Batch import Batch
from Commands.BatchCommands.BatchCommand import BatchCommand


class BatchCreation(BatchCommand):
    def execute(self, *args):
        if len(args) != 1:
            return 'need one parameter after the "batch" command represents batch name'
        batch_cli = Batch()
        batch_cli.start()
        new_batch = batch_cli.get_all_commands()
        BatchCommand.batches_dict[args[0]] = new_batch
        return ''
