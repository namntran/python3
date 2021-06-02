class DNS:
    # constructor
    def __init__(self):
        self.dns = dict()

    # add domain to IP address
    def add_DomainIPA(self, domain, ipa):
        self.dns[domain] = ipa

    # If no record found, return None
    def find_Domain(self, domain):
        if domain not in self.dns:
            return None
        return self.dns.get(domain)

# help menu to list available commands for user
def helpMenu():
    print("Available commands are 'find', 'add', 'quit',")

# welcome message
print('Welcome to DNS Server')
print('Type help for available commands')
# variable to store new DNS record
dns = DNS()

# use sentinel pattern
while True:
    # ask user for input
    userInput = input('$$$ ')
    # call helpMenu() function to print available commands
    if userInput.lower() == 'help':
        helpMenu()

    # find DNS record
    elif userInput.lower() == 'find':
        # ask for user input
        domain = input('Enter domain: ')
        # no record found
        if dns.find_Domain(domain) == None:
            print('No record found')
        else: # if record found, print domain name
            print('IP Address ' + dns.find_Domain(domain))

    # add DNS record
    elif userInput.lower() == 'add':
        # ask for user input
        domain = input('Enter domain: ')
        # ask for user input
        ipa = input('Enter IP Address: ')
        # add domain name and IP address record from user input
        dns.add_DomainIPA(domain, ipa)

    # quit and exit program
    elif userInput.lower() == 'q' or 'quit':
        print("Goodbye")
        break

    # catch all other user inputs
    else:
        print('Bad command')