class CLI:

    def __init__(self, prompt=''):
        self.prompt = prompt
        self.cli_live = True

    def start(self):
        while self.cli_live:
            command_string = input(self.prompt)
            if command_string == '': continue
            result = self.handle_command(command_string)
            if result != '':
                print(result)

    def handle_command(self, command_string):
        pass
