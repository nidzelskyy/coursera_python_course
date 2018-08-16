class Singelton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)

        return cls.instance

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email

a = Singelton()
b = Singelton()

print(a is b)


jane = User('Jane Doe', 'j.doe@example.com')
joe = User('Joe Doe', 'j.doe@example.com')

print(jane)
print(jane == joe)

print(hash(jane))
print(hash(joe))

user_email_map = {user: user.name for user in [jane, joe]}

print(user_email_map)
