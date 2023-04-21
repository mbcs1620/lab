class Account:
    
    def __init__(self, name: str) -> None:
        """
        Function to set up account object.
        :param name: Account name.
        """
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount: float) -> bool:
        """
        Function to make a deposit into account.
        :param amount: Deposit amount.
        :return: True indicates transaction success. False indicates transaction failure.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount: float) -> bool:
        """
        Function to make withdraw from account.
        :param amount: Withdraw amount.
        :return: True indicates transaction success. False indicates transaction failure.
        """
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            return False


    def get_name(self) -> str:
        """
        Method to access the account name.
        :return: Account name.
        """
        return self.__account_name
    
    def get_balance(self) -> float:
        """
        Method to access the account balance.
        :return: Account balance.
        """
        return self.__account_balance