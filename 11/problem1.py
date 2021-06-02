class DNS:
    # constructor
    def __init__(self):
        self.dns = dict()
        # self.blocklist = []

    # domain to IPA
    def add_DomainIPA(self, domain, ipa):
        self.dns[domain] = ipa

    # If no record, return None
    def find_DomainIPA(self, domain):
        return self.dns.get(domain, None)

def helpMenu():
    print("Available commands are 'find', 'add', 'quit',")

print('Welcome to DNS Server')
print('Type help for available commands')

dns = DNS()

# use sentinel pattern
while True:
    userInput = input('$$$ ')

    if userInput == 'help':
        helpMenu()

    elif userInput == 'find':
        d = input('Enter domain: ')
        if dns.find_DomainIPA(d) == None:
            print('None')
        else:
            print('IPA ' + dns.find_DomainIPA(d))

    elif userInput == 'add':
        d = input('Enter domain: ')
        ipa = input('Enter IPA: ')
        dns.add_DomainIPA(d, ipa)

    else:
        print('Bad command')