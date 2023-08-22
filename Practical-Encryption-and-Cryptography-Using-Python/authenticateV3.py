from Crypto.Hash import SHA256
import sys

# set a variabele for the path to the accounts file
path = './accounts.txt'

def calculate_salted_hash(password):
    salt = 'Skills for hire is fantastic!'
    salty_password = password + salt
    # pycryptodome requires you encode your string into utf-8 formatting
    # https://en.wikipedia.org/wiki/UTF-8
    salted_password = salty_password.encode('utf-8')
    h = SHA256.new()
    h.update(salted_password)
    return h.hexdigest()

def check_user_name(user_name):
    with open(path, 'r') as f:
        contents = f.read()
        if user_name in contents:
            print("Username in use.")
            sys.exit()
        return

def subscribe(user_name, password):
    account = f"{user_name} : {calculate_salted_hash(password)}"
    check_user_name(user_name)
    with open(path, 'a') as f:
        f.write(account + '\n')
    print("You are now registered!")

def login(user_name, password):
    authenticated = False
    with open(path, 'r') as f:
        hashed_password = calculate_salted_hash(password)
        accounts = f.readlines()
        for account in accounts:
            data = account.split(':')
            saved_username = data[0].strip()
            saved_password = data[1].strip()
            if user_name == saved_username and hashed_password == saved_password:
                authenticated = True
                break
            elif user_name == saved_username and hashed_password != saved_password:
                print("Invalid password.")
                break
        return authenticated
        

def main():
    # check to make sure file exists and if not generate file or the program will fail
    try:
        f = open(path, 'x')
    except:
        FileExistsError
    choice = input("Enter:\n1 - to subscribe\n2 - to login\n>>")
    if choice == '1':
        user_name = input('Enter a username:\n>>')
        password = input('Enter a password\n>>')
        subscribe(user_name, password)
    elif choice == '2':
        user_name = input('Username:\n>>')
        password = input('Password:\n>>')
        logged_on = login(user_name, password)
        if logged_on:
            print('[+]Logging into CNC server...\n[+]Connected...')
        else:
            print("Expect us.")
    else:
        print('Invalid choice')
    
main()
    
    
