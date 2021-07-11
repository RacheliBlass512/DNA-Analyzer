from CLI.CLI import CLI


class Confirm(CLI):
    def __init__(self):
        super().__init__('> confirm >>>')
        self.key_pressed = ''

    def start(self):
        super().start()

    def handle_command(self, command_string):
        if command_string in ['y', 'Y']:
            self.cli_live = False
            self.key_pressed = 'y'
        elif command_string in ['n', 'N']:
            self.cli_live = False
            self.key_pressed = 'n'
        else:
            return 'You have typed an invalid response. Please either confirm by \'y\'/\'Y\', or cancel by \'n\'/\'N\'.'
        return ''

    def get_is_ok(self):
        return self.key_pressed == 'y'
