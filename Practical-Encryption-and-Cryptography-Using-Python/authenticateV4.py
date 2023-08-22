# A clone of the version 3 with added functionality, but with extensive notes explaining the why and how of the entire program

from Crypto.Hash import SHA256
import sys

# set a variabele for the path to the accounts file as we will refernce this a number of times.
path = './accounts.txt'

def calculate_salted_hash(password):
    # salt is literally just a designated string appended to the string being hashed
    # so that hackers need both the salt and the hashed password to break it.
    # But we aren't so salty about being in this program, so I choose:
    salt = 'Skills for hire is fantastic!'
    # append the salt to the password
    salty_password = password + salt
    # pycryptodome requires you encode your string into utf-8 formatting
    # https://en.wikipedia.org/wiki/UTF-8
    salted_password = salty_password.encode('utf-8')
    # create the variable representing the hashing algorithm
    h = SHA256.new()
    # update it with the password
    h.update(salted_password)
    # Return the printable digest of the message that has been hashed so far. 
    return h.hexdigest()

def check_user_name(user_name):
    with open(path, 'r') as f:
        contents = f.read()
        # See if the user_name appears anywhere within the txt file.
        if user_name in contents:
            print("Username in use.")
            # the sys library is included by default with python and offers a clean way to close a program
            sys.exit()
        return

def subscribe(user_name, password):
    account = f"{user_name} : {calculate_salted_hash(password)}"
    check_user_name(user_name)
    # The original version wrote a new file everytime you subscribed someone new, deleting the previous subscriber. 
    # I changed the with(open, 'option') to append, which had the unexpected consequence of my program failing to run 
    # if the accounts.txt file wasn't present in the path at runtime. 
    # To see my solution check out the first few lines-of-code in main()
    with open(path, 'a') as f:
        f.write(account + '\n')
    print("You are now registered!")

def login(user_name, password):
    # This function returns a boolean value (t/f) to main()
    authenticated = False
    with open(path, 'r') as f:
        hashed_password = calculate_salted_hash(password)
        # Each account is on a seperate line in the txt file, readlines() allows us to turn the lines into a list object
        # There are other ways of doing this. I choose this one because it was easy.
        accounts = f.readlines()
        # By using the for statement I iterate through each of the lines in the text file.
        for account in accounts:
            # split(':') seperates the values on each line by the ':' creating a list of the split objects.
            data = account.split(':')
            # The username is list item zero.
            saved_username = data[0].strip()
            # The password is list item one.
            saved_password = data[1].strip()
            # if the username and password are correct:
            if user_name == saved_username and hashed_password == saved_password:
                authenticated = True
                # if authenticated we don't need to check against the user logging in against the
                # remaining usernames and hashed passwords.
                # We exit the loop with the break statement.
                break
            # If the username is correct, but the password is wrong:
            elif user_name == saved_username and hashed_password != saved_password:
                print("Invalid password.")
                # The login failed, so we break out of the loop.
                break
            # else: NOTHING. The default for authenticated is false. This loop should be allowed to run until
            # it finds a match (good or bad) and breaks out of the loop, 
            # or it goes through all the users and returns false to the main function.
        return authenticated
        

def main():
    # Check to make sure file exists and if not generate the file, or the program will fail
    # using 'a' without the referenced file present causes the program to fail.
    # Solution:
        # The open() option 'x' tests if the file exists. If the file doesn't the open function will create the file.
        # If the file exists it produces a FileExistsError, so we use a try except statement to allow
        # the program to execute properly if the file is present and an error is generated.
    try:
        f = open(path, 'x')
    except:
        FileExistsError
    # Prompt the user to select login or subscribe.
    choice = input("Enter:\n1 - to subscribe\n2 - to login\n>>")
    # If subscribe
    if choice == '1':
        user_name = input('Enter a username:\n>>')
        password = input('Enter a password\n>>')
        subscribe(user_name, password)
    # If login:
    elif choice == '2':
        user_name = input('Username:\n>>')
        password = input('Password:\n>>')
        logged_on = login(user_name, password)
        # If logged on is equal to true:
        if logged_on:
            print('[+]Logging into CNC server...\n[+]Connected...')
            sys.exit()
        # If the login fails inform the user we aren't pleased with them:
        else:
            print("Expect us.")
            sys.exit()
    # if anything but 1 or 2 is offered by the user as input:
    else:
        print('Invalid choice')
        sys.exit()
    
main()
    
