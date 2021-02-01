from SOLID_principles.OCP.violation.account_type import AccountType


class DebitAccount:

    @staticmethod
    def debit(value: float, account: str, account_type: AccountType):

        if account_type.name == "CurrentAccount":
            print('Debit current account')
        elif account_type.name == "SavingsAccount":
            print('Validates Account Anniversary')
            print('Debit Savings Account')
        else:
            print('Invalid account type')
            return
