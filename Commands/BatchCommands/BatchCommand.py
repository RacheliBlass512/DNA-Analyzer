from Commands.Command import Command


class BatchCommand(Command):
    def __init__(self):
        self.batches_dict = {}

    def execute(self, *args):
        pass
