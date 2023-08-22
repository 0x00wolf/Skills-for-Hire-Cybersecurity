# After I updated the program to python3.10
from Crypto.Hash import SHA256

def calculate_hash(password):
    password_to_hash = password.encode('utf-8')
    h = SHA256.new()
    h.update(password_to_hash)
    return h.hexdigest()

def subscribe(user_name, password):
    account = f"{user_name} : {calculate_hash(password)}"
    with open('account.txt', 'w') as f:
        f.write(account)
    # print(account)
    print("You are now registered!")

def login(user_name, password):
    with open('account.txt', 'r') as f:
        hashed_password = calculate_hash(password)
        account = f.read()
        data = account.split(':')
        saved_username = data[0].strip()
        # print(f"savedusername: {saved_username}")
        # print(f'hashed_password: {hashed_password}')
        saved_password = data[1].strip()
        if user_name == saved_username and hashed_password == saved_password:
            print("You are authenticated.")
        else:
            print("Invalid username or password.")

def main():
    choice = input("Enter:\n1 - to subscribe\n2 - to login\n>>")

    if choice == '1':
        user_name = input('Enter a username:\n>>')
        password = input('Enter a password\n>>')
        subscribe(user_name, password)
    elif choice == '2':
        user_name = input('Username:\n>>')
        password = input('Password:\n>>')
        login(user_name, password)
    else:
        print('Invalid choice')
    
main()
    
