from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    __LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    __CLIENT_TYPES = {"Student": Student, "Adult": Adult}
    __LOAN_CLIENT_MATCH = {"StudentLoan": "Student", "MortgageLoan": "Adult"}

    def __init__(self, capacity: int):
        self.capacity = capacity  # The number of clients а Bank can have.
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        self.granted_loans = []

    def add_loan(self, loan_type: str):
        """The method creates a loan of the given type and adds it to the loans' collection."""

        if loan_type not in self.__LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.__LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        """The method creates a client of the given type and adds them to the clients' collection."""

        if client_type not in self.__CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        new_client = self.__CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def __match_loan_to_client(self, loan: BaseLoan, client: BaseClient):
        """The student client can get only a student type of loan and the adult client
        can get only a mortgage type of loan."""

        if not self.__LOAN_CLIENT_MATCH[loan.loan_type] == client.client_type:
            raise Exception("Inappropriate loan type!")

    def grant_loan(self, loan_type: str, client_id: str):
        """The method adds the loan of the given type to the client’s loans collection.
        Both loan and client will always exist."""

        loan = [loan for loan in self.loans if loan.loan_type == loan_type][0]
        client = [client for client in self.clients if client.client_id == client_id][0]

        self.__match_loan_to_client(loan, client)

        self.loans.remove(loan)
        self.granted_loans.append(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        """The method removes the client with the given ID from the bank."""

        try:
            client = next(client for client in self.clients if client.client_id == client_id)
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        """The method increases the interest rates for all loans of the given type
        that are in the bank’s loan collection."""

        filtered_loans = [loan for loan in self.loans if loan.loan_type == loan_type]
        for loan in filtered_loans:
            loan.increase_interest_rate()

        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        """The method increases the interest rates for all clients that are in the bank’s client collection
        who currently have an interest rate less than the min_rate value."""

        filtered_clients = filter(lambda x: x.interest < min_rate, self.clients)
        client_count = 0
        while True:
            try:
                client = next(filtered_clients)
                client.increase_clients_interest()
                client_count += 1
            except StopIteration:
                return f"Number of clients affected: {client_count}."

    def get_statistics(self):
        """Returns information about the bank’s loans and its clients. Each string is on a new line."""
        try:
            avg_client_interest_rate = sum(client.interest for client in self.clients) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        text = (
            f"Active Clients: {len(self.clients)}\nTotal Income: {sum(client.income for client in self.clients) :.2f}\n"
            f"Granted Loans: {len(self.granted_loans)}, Total Sum: {sum(loan.amount for loan in self.granted_loans) :.2f}\n"
            f"Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans) :.2f}\n"
            f"Average Client Interest Rate: {avg_client_interest_rate :.2f}"
        )

        return text
