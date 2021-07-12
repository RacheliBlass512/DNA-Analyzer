from CLI.CLI import CLI
from Commands.BatchCommands.BatchCreation import BatchCreation
from Commands.SequenceAnalysisCommands.RegularFindCommand import RegularFindCommand
from Commands.SequenceAnalysisCommands.findallCommand import findallCommand
from Commands.SequenceCreationCommands.DupCommand import DupCommand
from Commands.SequenceCreationCommands.LoadCommand import LoadCommand
from Commands.SequenceCreationCommands.NewCommand import NewCommand
from Commands.SequenceManagementCommands.DelCommand import DelCommand
from Commands.SequenceManagementCommands.SaveCommand import SaveCommand
from Commands.SequenceManipulationCommands.ReplaceCommand import ReplaceCommand
from Commands.SequenceManipulationCommands.SliceCommand import SliceCommand
from Commands.helper_functions_command import not_valid_str


class CMD(CLI):
    def __init__(self):
        super().__init__('> cmd >>>')
        self.commands_dict = {
            'new': NewCommand(),
            'load': LoadCommand(),
            'dup': DupCommand(),
            'slice': SliceCommand(),
            'replace': ReplaceCommand(),
            'del': DelCommand(),
            'save': SaveCommand(),
            'find': RegularFindCommand(),
            'findall': findallCommand(),
            'batch': BatchCreation()
        }

    def start(self):
        super().start()

    def handle_command(self, command_string):
        parts = command_string.split()
        command_type = parts[0]
        if command_type in self.commands_dict:
            result = self.commands_dict[command_type].execute(*parts[1:])
            return result
        else:
            return not_valid_str
