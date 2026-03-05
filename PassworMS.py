import hashib
import getpass

password_manager = {}

def create_account {}:
    username = Imput("Enter your desired username:  ")
    password = getpass.getpass("Enter your desired password:  ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account Created Succesfully")

def login{}:
    username = Imput("Enter your username:  ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successfull")
    else:
        print("Invalid Username or Password")

def main{}:
    while True:
        choice = Imput("Enter 1 to create an account, 2 to login, or 0 to exti:  ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()