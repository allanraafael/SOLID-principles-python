
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
