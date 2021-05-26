class GoCard:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transaction_list = []

    def rideTicket(self, cost):
        self.balance -= cost
        transaction = ["Ride", cost, self.balance]
        self.transaction_list.append(transaction)

    def topUp(self, amount):
        self.balance += amount
        transaction = ["Top up", amount, self.balance]
        self.transaction_list.append(transaction)

    def getBalance(self):
        return self.balance

    def printStatement(self):
        print("Statement: ")
        print("{:<10} {:>20} {:>20}".format("event","amount ($)","balance ($)"))
        for e, a, b in self.transaction_list:
            print("{:<10} {:>20} {:>20}".format(e, a, b))
        print("Final balance:{:>38}".format(b))

while True:
    try:
        userInput = input("Creating account. Input initial balance: ")
        userAccount = GoCard(float(userInput))
        break
    except:
        print("Enter a valid number")

while True:
    userInput = input("? ")
    if userInput == "q":
        userAccount.printStatement()
        break

    userInput_list = userInput.split(" ")

    if len(userInput_list) == 2:
        try:
            if userInput_list[0] == "r":
                userAccount.rideTicket(float(userInput_list[1]))
            elif userInput_list[0] == "t":
                userAccount.topUp(float(userInput_list[1]))
            else:
                print("Bad command.")
        except:
            print("Enter a valid input")

    elif len(userInput_list) == 1:
        try:
            if userInput_list[0] == "b":
                print("Balance = $", userAccount.getBalance())
            elif userInput_list[0] == "r":
                print("Bad command.")
            elif userInput_list[0] == "t":
                print("Bad command.")
            else:
                print("Bad command.")
        except:
            print("Enter a valid input")