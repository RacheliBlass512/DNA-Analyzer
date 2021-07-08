from commands import NewCommand, LoadCommand, DupCommand

commands_dict = {
    'new': NewCommand(),
    'load': LoadCommand(),
    'dup': DupCommand()
}
not_valid_str = "not valid command"


class CLI:

    def start(self):
        while True:
            command_string = input('> cmd >>>')
            if command_string == '': continue
            parts = command_string.split()
            command_type = parts[0]
            if command_type in commands_dict:
                result = commands_dict[command_type].execute(*parts[1:])
                print(result)
            else:
                print(not_valid_str)
