"""
In this program, we define a BankAccount class with two private attributes, __account_number and __balance.
These attributes are encapsulated and cannot be accessed directly from outside the class. Instead,
we provide two public methods, get_account_number() and get_balance(), to retrieve these attributes.

We also define two methods, deposit() and withdraw(), to modify the __balance attribute. These methods ensure
that the balance is updated correctly and that withdrawals cannot be made if the account has insufficient funds.

In the main part of the program, we create a BankAccount object and use the public methods to interact with it.
We cannot access the private attributes directly, but we can use the public methods to retrieve their values and modify
them indirectly. This is an example of encapsulation, where the implementation details of the class are hidden from the
outside world and can only be accessed through a well-defined public interface.
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful. New balance is:", self.__balance)

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.__balance -= amount
            print("Withdrawal successful. New balance is:", self.__balance)

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance


# Create a BankAccount object
my_account = BankAccount("12345", 1000)

# Try to access private attribute directly (will raise an AttributeError)
# print(my_account.__balance)

# Access private attribute using public method
print("My account balance is:", my_account.get_balance())

# Deposit money
my_account.deposit(500)

# Withdraw money
my_account.withdraw(200)

# Try to withdraw more money than available balance
my_account.withdraw(2000)

