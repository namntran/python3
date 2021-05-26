# develop a class for a Go Card Account that maintains a balance
# subtract the cost of ticket/ ride, add top up amount, print the balance

class GoCard:
    def __init__(self, initial_balance):
        """Create an account with initial balance"""
        self.balance = initial_balance
        self.initial_balance = initial_balance
        # empty list to store transactions for event, amount, balance
        self.transaction_list = []

    def getBalance(self):
        """Return the current account balance"""
        return self.balance

    def rideTicket(self, cost):
        """Subtract cost of ticket from balance and add to transaction list"""
        self.balance -= cost
        # store value for ride
        transaction = ["Ride", cost, self.balance]
        # update the transaction
        self.transaction_list.append(transaction)

    def topUp(self, amount):
        """Update the account balance and add to transaction list"""
        self.balance += amount
        # store value for top up
        transaction = ["Top up", amount, self.balance]
        # update the transaction
        self.transaction_list.append(transaction)

    # def printStatement(self):
    #     """Return the current account balance"""
    #     # print the first row
    #     print("Statement: ")
    #     # print the headings for event, amount, balance
    #     print("{:<10} {:>20} {:>20}".format("event","amount ($)","balance ($)"))
    #     # use for loop to traverse the event, amount, balance values stored in transaction list and print
    #     print("Initial balance{:>37}".format(self.initial_balance))
    #     for e, a, b in self.transaction_list:
    #         print("{:<10} {:>20} {:>20}".format(e, a, b))
    #     # print the balance in the last row
    #     print("Final balance{:>39}".format(b))

# use sentinel pattern
while True:
    try:
        # request user input
        userInput = float(input("Creating account. Input initial balance: "))
        userAccount = GoCard(userInput)
        break
    except:
        print("Enter a valid number")
# use sentinel pattern
while True:
    userInput = input("? ")
    # user enters q to exit program
    if userInput == "q":
        # userAccount.printStatement()
        break

    # split input string
    userInput_list = userInput.split(" ")
    # check the first element of the user input if there are 2 elements
    if len(userInput_list) == 2:
        try:
            # get user input and call the rideTicket() method
            if userInput_list[0] == "r":
                userAccount.rideTicket(float(userInput_list[1]))
            # get user input and call the topUp() method
            elif userInput_list[0] == "t":
                userAccount.topUp(float(userInput_list[1]))
            else:
                # check user input to catch any other command
                print("Bad command.")
        except:
            print("Enter a valid input")
    # check the user input
    elif len(userInput_list) == 1:
        try:
            # get user input and call the getBalance() method
            if userInput_list[0] == "b":
                print("Balance = $", userAccount.getBalance())
            # check user input, since only 1 element for r or t then no value is assigned. print bad command
            elif userInput_list[0] == "r":
                print("Bad command.")
            elif userInput_list[0] == "t":
                print("Bad command.")
            else:
                # check user input to catch any other command
                print("Bad command.")
        except:
            print("Enter a valid input")