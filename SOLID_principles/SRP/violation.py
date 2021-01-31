import sqlite3
import yagmail


class Client:
    """
    Class receiving many responsibilities, violates the Single Responsibility Principe (SRP)
    """

    def __init__(self, name, email, cpf, date_register):
        """
        Representing an entity that has the properties name, email, cpf and registration date
        """

        self.name = name
        self.email = email
        self.cpf = cpf
        self.date_register = date_register

    def add_client(self):
        """
        Function that is receiving many responsibilities:
         * Validates email and CPF;
         * Add to the database;
         * Sending email;
         * Displaying message of success.
        """

        if "@" not in self.email:
            print("Client with invalid email")
            return

        if len(self.cpf) != 11:
            print("Client with invalid CPF")
            return

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        table_name = 'client'
        column_name = 'name'
        column_email = 'email'
        column_cpf = 'cpf'
        column_date_register = 'date_register'
        sqlite_insert_query = f"INSERT INTO {table_name} ({column_name}, {column_email}, {column_cpf}, " \
                              f"{column_date_register}) VALUES ('{self.name}', '{self.email}', '{self.cpf}'," \
                              f" '{self.date_register}');"
        cursor.execute(sqlite_insert_query)
        conn.commit()
        conn.close()

        # replace by your gmail credentials
        user = ''
        password = ''

        # If it fails, activate for less secure app access: https://www.google.com/settings/security/lesssecureapps
        yag = yagmail.SMTP(
            user=user,
            password=password,
        )
        contents = ['Congratulations! You are registered.']
        yag.send(self.email, 'You welcome.', contents)

        return "Client successfully registered!"
