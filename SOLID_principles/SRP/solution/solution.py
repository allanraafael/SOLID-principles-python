from SOLID_principles.SRP.solution.client import Client
from SOLID_principles.SRP.solution.client_services import ClientServices


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
        client_service = ClientServices()

        # persists in the database and send email
        client_service.add_client(client)
