class DNS:
    # constructor and initialise
    def __init__(self):
        self.dns = dict()

    # add domain to IP address
    def add_DomainIPA(self, domain, ipa):
        self.dns[domain] = ipa

    # If no record found, return None
    def find_Domain(self, domain):
        if domain not in self.dns:
            return None
        else:
            return self.dns.get(domain)

# welcome message function to greet user
def welcomeMessage():
    print('Welcome to DNS Server')
    print('Type help for available commands')

# help menu function to list available commands for user if requested
def helpMenu():
    print("Available commands are 'find', 'add', 'quit',")

# test program allows user to test class by typing in fake domain names and IP addresses to update the DNS and domain names to lookup
def testProgram():
# use sentinel pattern
    while True:
        try:
            # ask user for input
            userInput = input('$$$ ')
            # convert user input to lower case, check if user enters help
            if userInput.lower() == 'help':
            # call helpMenu() function to print available commands
                helpMenu()

            # convert user input to lower case, check if user enters find
            elif userInput.lower() == 'find':
                # ask for user input
                domain = input('Enter domain: ')
                # no record found
                if dns.find_Domain(domain) == None:
                    print('No record found')
                else: # if record found, print domain name
                    print('IP Address ' + dns.find_Domain(domain))

            # convert user input to lower case, check if user enters add DNS record (domain and IP address)
            elif userInput.lower() == 'add':
                # ask for user input
                domain = input('Enter domain: ')
                # ask for user input
                ipa = input('Enter IP Address: ')
                # add domain name and IP address record from user input
                dns.add_DomainIPA(domain, ipa)

            # quit and exit program
            elif userInput.lower() == 'quit':
                print("Goodbye")
                break

            # catch all other user inputs
            else:
                print('Bad command')
        except:
            print("Type help for valid command")

# variable to store new DNS record
dns = DNS()
# call welcome message function
welcomeMessage()
# call test program function
testProgram()