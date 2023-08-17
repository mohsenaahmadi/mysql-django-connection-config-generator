from mysql.connector import connect
from mysql.connector import Error

# Database connection parameters
db_config = {
    "host": "localhost",  # Replace with your MySQL host
    "user": "dbadmin",  # Replace with your MySQL username
    "password": "Moh3en125$)!)",  # Replace with your MySQL password
    "database": "vahdat"  # Replace with your MySQL database name
}
connection = None
cursor = None


class MySqlConnectionChecker:
    def __init__(self, *args, **kwargs):
        self.db_config = {
            "host": kwargs['host'],  # Replace with your MySQL host
            "user": kwargs['username'],  # Replace with your MySQL username
            "password": kwargs['password'],  # Replace with your MySQL password
            "database": kwargs['database']  # Replace with your MySQL database name
        }
        self.connection = None
        self.cursor = None

    def test_connection(self):
        result = True
        try:
            # Create a MySQL database connection
            self.connection = connect(**self.db_config)

            # Check if the connection was successful
            if self.connection.is_connected():
                print("Connected to MySQL database")
                # Perform your database operations here
                # For testing, you can execute a simple query
                self.cursor = self.connection.cursor()
                self.cursor.execute("SELECT NOW()")
                result = self.cursor.fetchone()
                print("Current MySQL datetime:", result[0])

        except Error as e:
            print("Error connecting to MySQL database:", e)
            result = False

        finally:
            # Close the database connection
            if 'connection' in locals() and self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection closed")

        return result
