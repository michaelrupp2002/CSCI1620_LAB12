class Account:

    def __init__(self, name: str):
        """
        Function to initialize private variables account_name and account_balance.
        :param name: Name of account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to add funds to account_balance.
        :param amount: Amount to add.
        :return: True if successful and false if unsuccessful.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw funds from account_balance.
        :param amount: Amount to withdraw.
        :return: True if successful and false if unsuccessful.
        """
        if 0 < amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to get the current account_balance.
        :return: The balance of the account.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to get the name of the current account.
        :return: The name of the account.
        """
        return self.__account_name
