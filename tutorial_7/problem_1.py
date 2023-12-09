class BankAccount:
    number_of_account = 0

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.number_of_account += 1

    @staticmethod
    def displayTotalAccount():
        print(f"Total number of account created is {BankAccount.number_of_account}")

    def setBalance(self, balance: int):
        self.balance = balance

    def getBalance(self):
        print(self.balance)

    def withdraw(self, balance: int):
        if balance > self.balance:
            print("Balance is sufficient")
        self.balance -= balance

    def deposit(self, deposit: int):
        self.balance = deposit

    def __str__(self) -> str:
        return f"{self.name} has {self.balance} in the account."
