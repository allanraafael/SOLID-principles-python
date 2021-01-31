from SOLID_principles.connection.create_table_client import create_table_client
import sqlite3


def main():
    """
    Create table client only if it doesn't exist
    """

    conn = sqlite3.connect('database.sqlite')
    create_table_client(conn)


if __name__ == '__main__':
    main()
