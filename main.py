import sqlite3

from SOLID_principles.OCP.violation.violation import ViolationOCP
from SOLID_principles.SRP.solution.solution import SolutionSRP
from SOLID_principles.SRP.violation.violation import ViolationSRP
from SOLID_principles.connection.create_table_client import create_table_client


def main():
    """
    Main function that runs the project
    """

    conn = sqlite3.connect('database.sqlite')
    create_table_client(conn)  # Create table client only if it doesn't exist

    # violation_srp = ViolationSRP()
    # violation_srp.violation()
    # solution_srp = SolutionSRP()
    # solution_srp.solution()  # Solution for SRP completed from the violation found in the ViolationSRP class

    # violation_ocp = ViolationOCP()
    # violation_ocp.violation()


if __name__ == '__main__':
    main()
