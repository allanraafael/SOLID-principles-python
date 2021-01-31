from SOLID_principles.SRP.solution.client import Client
from SOLID_principles.SRP.solution.client_repository import ClientRepository
from SOLID_principles.SRP.solution.cpf_services import CPFServices
from SOLID_principles.SRP.solution.email_services import EmailServices
from SOLID_principles.config.settings import auth_user, auth_password


class ClientServices:
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
            user=user,
            password=password
        )

        print("Client successfully registered!")
