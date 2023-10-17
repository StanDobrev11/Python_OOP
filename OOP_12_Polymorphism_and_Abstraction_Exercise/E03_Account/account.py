from typing import List, Iterator


class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self.balance = amount
        self._transactions: List[int] = []

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value) -> None:
        self._balance = value

    def add_transaction(self, transaction_amount: int) -> str:
        if not isinstance(transaction_amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(transaction_amount)

    def handle_transaction(self, transaction_amount: int) -> str:
        new_balance = self.balance + transaction_amount
        if new_balance < 0:
            raise ValueError("sorry cannot go in debt!")

        self.balance = new_balance
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __iter__(self) -> Iterator[int]:
        return iter(self._transactions)

    def __getitem__(self, item_idx: int) -> int:
        return self._transactions[item_idx]

    def __gt__(self, other: "Account") -> bool:
        return self._balance > other.balance

    def __ge__(self, other: "Account") -> bool:
        return self._balance >= other.balance

    def __eq__(self, other: "Account") -> bool:
        return self._balance == other.balance

    def __add__(self, other: "Account") -> "Account":
        new_instance = Account(f"{self.owner}&{other.owner}", sum([self.amount, other.amount]))
        new_instance._transactions = self._transactions + other._transactions
        return new_instance


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
