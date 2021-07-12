from CLI.CLI import CLI


class Batch(CLI):
    def __init__(self):
        super().__init__('> batch >>>')
        self.all_commands = []

    def start(self):
        super().start()

    def handle_command(self, command_string):
        if command_string == 'end':
            self.cli_live = False
        else:
            self.all_commands.append(command_string)
        return ''

    def get_all_commands(self):
        return self.all_commands
