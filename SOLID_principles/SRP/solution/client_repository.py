import sqlite3

from SOLID_principles.SRP.solution.client import Client


class ClientRepository:
    """Uses the repository pattern to encapsulate all operations that refer to the database"""

    @staticmethod
    def add_client(client: Client):
        """
        Some client persists in the database

        :param client:
            Client object
        """

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        table_name = 'client'
        column_name = 'name'
        column_email = 'email'
        column_cpf = 'cpf'
        column_date_register = 'date_register'
        sqlite_insert_query = f"INSERT INTO {table_name} ({column_name}, {column_email}, {column_cpf}, " \
                              f"{column_date_register}) VALUES ('{client.name}', '{client.email}', '{client.cpf}'," \
                              f"'{client.date_register}');"
        cursor.execute(sqlite_insert_query)
        conn.commit()
        conn.close()
