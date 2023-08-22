# The original program from the Pluralsight course unchanged.
from Crypto.Hash import SHA256


def calculate_hash(password):
    h = SHA256.new()
    h.update(password)
    return h.hexdigest()


def subscribe(user_name, password):
    account = user_name + ':' + calculate_hash(password)
    f = open('accounts.txt', 'w')
    f.write(account)
    f.close()
    print '[+]You are registered now!'


def login(user_name, password):
    f = open('accounts.txt', 'r')
    account_file = f.read()
    s = account_file.split(':')
    user_name_file = s[0]
    password_file = s[1]
    hashed_password = calculate_hash(password)

    if user_name == user_name_file and hashed_password == password_file:
        print 'You are Authenticated :)'
    else:
        print '[!]Invalid username or password'


def main():
    input = raw_input("Enter:\n 1] to subscribe\n 2] to Login\nChoice> ")

    if input == '1':
        user_name = raw_input("Enter a username: ")
        password = raw_input("Enter a password: ")
        subscribe(user_name, password)
    elif input == '2':
        user_name = raw_input("Enter a username: ")
        password = raw_input("Enter a password: ")
        login(user_name, password)
    else:
        print '[!]Invalid choice'


main()
