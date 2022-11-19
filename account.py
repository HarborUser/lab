class Account:
    def __init__(self, name: str) -> None:
        """
        This method is to initialize the values
        :param name: The name of the account
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This method deposits funds into a account
        :param amount: Amount to be deposited
        :return: False if the amount is not successful and True if it is successful
        """

        if amount < 0 or amount == 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        This method withdraws funds from the account
        :param amount: Amount to be withdraw
        :return: False if the amount is not successful and True if it is successful
        """
        if amount < 0 or amount == 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        This method returns the account balance
        :return: It returns account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        This method return the name of the account
        :return: It returns name of the account
        """
        return self.__account_name
