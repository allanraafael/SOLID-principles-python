from SOLID_principles.OCP.violation.account_type import AccountType
from SOLID_principles.OCP.violation.debit_account import DebitAccount


class ViolationOCP:

    @staticmethod
    def violation():
        current_type_account = AccountType('CurrentAccount')
        savings_type_account = AccountType('SavingsAccount')
        other_type_account = AccountType('')

        debit_account = DebitAccount()
        debit_account.debit(100, 'account_1', current_type_account)
