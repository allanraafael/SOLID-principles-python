from SOLID_principles.SRP.violation.client import Client


class ViolationSRP:
    """Violation SRP"""

    client = Client(
        name='test',
        email='wewal11647@poetred.com',
        cpf='00000000000',
        date_register='0000-00-00'
    )

    def violation(self):
        """Persists in the database and sends email using many responsibilities within the client class"""

        self.client.add_client()
