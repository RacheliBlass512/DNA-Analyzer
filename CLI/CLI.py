class CLI:

    def __init__(self, prompt=''):
        self.prompt = prompt

    def start(self):
        while True:
            command_string = input(self.prompt)
            if command_string == '': continue
            print(self.handle_command(command_string))

    def handle_command(self, command_string):
        pass
