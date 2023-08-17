from mysql_connector_checker import MySqlConnectionChecker
from utils import get_input

if __name__ == '__main__':
    mysql_obj = get_input()
    check_result = MySqlConnectionChecker(mysql_obj.related_kwargs())
    if check_result:
        mysql_obj.write_config_for_mysql_checker()
