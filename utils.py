from mysql_connector_checker import MySqlConnectionChecker
import getpass

class MySQLConf:
    def __init__(
            self, db_name: str,
            username: str,
            password: str,
            host: str = 'localhost',
            default_character_set: str = 'utf-8',
            port: str = '3306'
    ) -> None:
        self.database = db_name
        self.password = password
        self.username = username
        self.host = host
        self.port = port
        self.default_character_set = default_character_set
        if self.port is None:
            self.port = '3306'
        if self.host is None:
            self.host = 'localhost'
        if self.default_character_set is None:
            self.default_character_set = 'utf-8'
        self.path = __file__.replace('utils.py', 'db.cnf')

    @property
    def port_str(self):
        if self.port is None or self.port == '':
            return ''
        else:
            return ':' + self.port

    @property
    def host_str(self):
        if self.host is None or self.host == '':
            return 'localhost'
        else:
            return self.host

    @property
    def charset_str(self):
        if self.default_character_set is None or self.default_character_set == '':
            return 'utf-8'
        else:
            return self.default_character_set

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username}@{self.database} - {self.host_str}{self.port_str} IDENTIFIED By {self.password})"

    def related_kwargs(self):
        return vars(self)

    def write_config_for_mysql_checker(self):
        TerminalInputOutput.print_info_in_terminal(
            f'Enter Path for save config file.\n(Leave it blank for create in {self.path})')
        path = TerminalInputOutput.get_input_and_return_value()
        if path is not None and path != '':
            self.path = path
        with open(self.path, 'w+') as file:
            file.write('[client]\n')
            file.write(f'database = {self.database}\n')
            file.write(f'host = {self.host}\n')
            file.write(f'user = {self.username}\n')
            file.write(f'port = {self.port}\n')
            file.write(f'password = {self.password}\n')
            file.write(f'default-character-set = {self.default_character_set}\n')
        TerminalInputOutput.print_success_in_terminal(f'Write it successful in {self.path}.')


class TerminalInputOutput:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def print_error_in_terminal(message: str):
        print(TerminalInputOutput.FAIL + message + TerminalInputOutput.ENDC)

    @staticmethod
    def print_success_in_terminal(message: str):
        print(TerminalInputOutput.OKGREEN + message + TerminalInputOutput.ENDC)

    @staticmethod
    def print_info_in_terminal(message: str):
        print(TerminalInputOutput.OKCYAN + message + TerminalInputOutput.ENDC)

    @staticmethod
    def get_input_and_return_value(default_value_if_blank=None,required = False, is_password=False):
        value = ''
        if is_password:
            value = getpass.getpass()
        else:
            value = input()
        if value == '':
            if not required:
                return default_value_if_blank
            else:
                TerminalInputOutput.print_error_in_terminal("Empty Value not acceptable. Enter value.")
                return TerminalInputOutput.get_input_and_return_value(default_value_if_blank, required, is_password)
        return value


def get_input():
    TerminalInputOutput.print_info_in_terminal('Enter Database Schema name:')
    db_name = TerminalInputOutput.get_input_and_return_value(required=True)
    TerminalInputOutput.print_info_in_terminal('Enter Username:')
    username = TerminalInputOutput.get_input_and_return_value(required=True)
    TerminalInputOutput.print_info_in_terminal(f'Enter Password of {username}:')
    password = TerminalInputOutput.get_input_and_return_value(required=True, is_password=True)
    TerminalInputOutput.print_info_in_terminal(f'Enter host IP:\n(if is in this machine leave it blank.)')
    host = TerminalInputOutput.get_input_and_return_value()
    TerminalInputOutput.print_info_in_terminal(
        f'Enter MySql Access Port:\n(if port of MySql not change leave it blank.)')
    port = TerminalInputOutput.get_input_and_return_value()
    TerminalInputOutput.print_info_in_terminal(f'Enter default character set:\n("utf-8" is default.)')
    default_character_set = TerminalInputOutput.get_input_and_return_value(
    )
    return MySQLConf(**locals())


def get_yes_or_no():
    while True:
        answer = input().lower()
        if answer == 'y' or answer == 'n':
            if answer == 'y':
                return True
            else:
                return False
        TerminalInputOutput.print_error_in_terminal('Wrong Input.')
        continue


def run_script():
    mysql_obj = get_input()
    check_result = MySqlConnectionChecker(**mysql_obj.related_kwargs()).test_connection()
    if not check_result:
        TerminalInputOutput.print_info_in_terminal('Failed to connect db, Do you want to bypass?(y/n)')
        check_result = get_yes_or_no()
    if check_result:
        mysql_obj.write_config_for_mysql_checker()
        TerminalInputOutput.print_success_in_terminal('All Done! Good Bye.')
    else:
        TerminalInputOutput.print_error_in_terminal('Failed to create. See you next time! :)')

