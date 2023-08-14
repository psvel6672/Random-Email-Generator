import random, string

class RandomEmail:
    
    def __init__(self):

        print("Random Email Id Generator - V1.0")
        
        self.emailDomains = ["gmail.com", "yahoo.com", "outlook.com"]
        self.usrNameLength = random.randint(8, 10)
        
    def _generateEmail(self):
        
        username = ''.join(random.choice(string.ascii_letters) for _ in range(self.usrNameLength))
        domain = random.choice(self.emailDomains)

        email = f"{username}@{domain}"
        return email
    
    def runModule(self):
        
        random_email = self._generateEmail()
        print("EMail :: "+str(random_email.lower()))

mod = RandomEmail()
mod.runModule()
