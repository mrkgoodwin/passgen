class Storage:
    filename = "passwords.txt"
    contents = {
        'Yeet': 'abc123',
        'Leet': 'abc123',
    }

    def __init__(self, filename):
        self.filename = filename
        # open file, decrypt it, put them into self.contents

    def set(self, key, value):
        self.contents[key] = self.encrypt(value)
        return True

    def get(self, key):
        return self.contents[key]

    def save(self):
        # take self.contents, encrypt it, put it back into file self.filename
        return True

    def decrypt(self, value):
        return True

    def encrypt(self, value):
        return True


passwordStorage = Storage("passwords.txt")

# python main.py set mypassword whatever

passwordStorage.set("mypassword", "whatever")