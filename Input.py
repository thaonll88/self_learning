def get_selection():
    op = input("Enter d for deposit, w for withdrawal, s for show, or q to quit: ")
    if op != "d" and op != "w" and op != "s" and op != "q":
        print("Invalid type. Please try again")
        op = None
    return op


def get_amount():
    amount = None
    try:
        amount = int(input("Enter amount: "))
        if amount <= 0:
            print("The amount must be positive.")
            amount = None
    except:
        print("invalid amount. Please try again.")

    return amount
