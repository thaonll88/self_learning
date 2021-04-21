import Input
import account


def main():
    print("Welcome to the atm.")
    while True:
        amount = None
        selection = Input.get_selection()
        if selection == "q":
            break
        elif selection == "s":
            account.Account().show_balance()
        elif selection is not None:
            amount = Input.get_amount()

        if amount is None:
            pass
        elif selection == "d":
            account.Account().deposit(amount)
        else:
            account.Account().withdrawal(amount)


main()