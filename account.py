import os
import Input


def get_current_balance(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write("0")
            return 0
    else:
        if os.stat(file_name).st_size == 0:
            with open(file_name, "w") as file:
                file.write("0")
            return 0
        else:
            with open(file_name, "r+") as file:
                def intTryParse(value):
                    try:
                        return int(value)
                    except ValueError:
                        return value
                line = intTryParse(file.readline())
            if not isinstance(line, int):
                with open(file_name, "w+") as file:
                    file.write("0")
                return 0
            else:
                with open(file_name, "r") as file:
                    return int(file.read())


class Account:
    balance = None

    def __init__(self):
        self.balance = get_current_balance("balance.txt")

    def show_balance(self):
        print("Your current balance is: ", self.balance)

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have that much!")
        else:
            # update self.balance
            self.balance -= amount
            print("Withdraw $%d." % amount)
            # update file balance
            with open("balance.txt", "w+") as file:
                file.write(str(self.balance))

    def deposit(self, amount):
        # update self.balance
        self.balance += amount
        print("Deposit $%d." % amount)
        # update file balance
        with open("balance.txt", "r+") as file:
            file.write(str(self.balance))
