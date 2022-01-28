from termcolor import colored

class wongwongprint(object):
    @staticmethod
    def info(str):
        print(colored(f"[Info] ", 'green') + str)

    @staticmethod
    def warn(str):
        print(colored(f"[Warning] ", 'yellow') + str)

    @staticmethod
    def error(str):
        print(colored(f"[Error] ", 'red') + str)

    @staticmethod
    def finish(str):
        print(colored(f"[Finished] ", 'cyan') + str)

    @staticmethod
    def undefined(str):
        print(colored(f"[Finished] ", 'magenta') + str)