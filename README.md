# MySQL Database Connection File Generator for Django

## Introduction

This Python script simplifies the process of generating a MySQL database connection file,
guiding you through the necessary steps to create a configuration file for connecting to a MySQL database,
specifically tailored for setting up a connection in Django settings. It also includes a feature to test the MySQL
connection to ensure that it's configured correctly.

## Prerequisites

Before using this script, ensure that you have the following prerequisites installed:

- Python 3.x
- MySQL Connector/Python library

You can install the required dependencies using the following commands:

```bash
pip install mysql-connector-python==8.1.0
```

The mysql-connector-python package will also install the necessary protobuf library as a dependency.

## Usage

To generate a MySQL database connection file, follow these steps:

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command:

```bash
python create_mysql_conf.py
```

After running the script, you will be prompted to provide the required information, including:

- MySQL database name
- MySQL username
- MySQL password
- MySQL host (optional, default is localhost)
- MySQL port number (optional, default is 3306)
- MySQL default character set (optional, default is utf-8)
- Name for the connection configuration file

The script will create a configuration file with the specified name (e.g., `db.cnf`) in the same directory.
This file will contain the database connection details in the following format:

```ini
[client]
database = your_mysql_database
host = your_mysql_host
user = your_mysql_username
port = your_mysql_port
password = your_mysql_password
default-character-set = utf-8
```

## Using the Configuration in Django

To integrate the generated `db.cnf` configuration file into a Django project's `settings.py`, follow these steps:

1. Open your Django project's `settings.py` file.

2. Locate the DATABASES configuration within your settings.py file. Replace the existing database configuration or add
   a new database entry as needed.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'db.cnf'),
        },
    }
}
```
* Ensure that the 'read_default_file' option points to the correct path for your `db.cnf` file. In this example,
it assumes that the sb.cnf file is located in the same directory as your settings.py file.
With this configuration in place, your Django project will use the MySQL database settings provided in the db.cnf file.
This approach offers the benefits of keeping your database configuration separate, secure, and consistent across different environments.

You can now seamlessly manage your MySQL database connections in your Django application.

## License

This script is open-source and free to use by everyone. You can find the license information in the `LICENSE` file.

## Acknowledgments

Special thanks to the MySQL Connector/Python developers and the open-source community for their contributions to the
MySQL Connector/Python library.
