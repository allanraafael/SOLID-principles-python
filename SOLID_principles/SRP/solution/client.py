
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
