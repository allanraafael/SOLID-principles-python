import sqlite3
import yagmail
from SOLID_principles.config.settings import auth_user, auth_password


class Client:
    """
    Class receiving only the responsibility of representing a real world client entity,
    respecting the Single Responsibility Principe (SRP)
    """

    def __init__(self, name, email, cpf, date_register):
        """Representing an entity that has the properties name, email, cpf and registration date"""

        self.name = name
        self.email = email
        self.cpf = cpf
        self.date_register = date_register

    def __str__(self):
        return self.name


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


class EmailServices:
    """Handles only email-related services"""

    @staticmethod
    def is_valid(email: str):
        """
        Check if the email parameter is valid

        :param email:
            String must be in email format to be valid
        """

        return "@" in email

    @staticmethod
    def send(to: str, subject: str, message: list[str], user, password):
        """
        Sends the email

        :param to:
            Email sending destination
        :param subject:
            Summary of what will be informed in the email
        :param message:
            Email body
        :param user:
            replace by your gmail credentials
        :param password:
            replace by your gmail credentials
        """

        # If it fails, activate for less secure app access: https://www.google.com/settings/security/lesssecureapps
        yag = yagmail.SMTP(user=user, password=password)
        yag.send(to, subject, message)


class CPFServices:
    """Handles only cpf-related services"""

    @staticmethod
    def is_valid(cpf: str) -> bool:
        """
        Check if the cpf parameter is valid

        :param cpf:
            String must have the number of characters in a cpf
        """

        return len(cpf) == 11


class ClientService:
    """
    Manipulates the services of a client, checking if the data is valid and, if they are, an instance of the
    ClienteRepository will be called and keeps it in the bank.
    """

    @staticmethod
    def is_valid(client: Client) -> bool:
        """
        Check if email and cpf are valid

        :param client:
            Client object
        """

        return EmailServices.is_valid(client.email) and CPFServices.is_valid(client.cpf)

    def add_client(self, client: Client):
        """
        The service of adding a client consists of persisting in the database and sending email

        :param client:
            Client object
        """

        if not self.is_valid(client):
            print("Invalid data")
            return

        repo = ClientRepository()
        repo.add_client(client)

        # Your gmail credentials
        user = auth_user
        password = auth_password

        EmailServices.send(
            to=client.email,
            subject="You welcome.",
            message=['Congratulations! You are registered.'],
            auth_user=user,
            auth_password=password
        )

        print("Client successfully registered!")


class SolutionSRP:
    """Resolves violations: SRP, from the violation.py module"""

    @staticmethod
    def solution():
        """Invokes the execution of the solution"""

        client = Client(
            name='test',
            email='wewal11647@poetred.com',
            cpf='00000000000',
            date_register='0000-00-00'
        )
        client_service = ClientService()

        # persists in the database and send email
        client_service.add_client(client)
