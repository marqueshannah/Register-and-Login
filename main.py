def select_login_signup():
    while True:
        selection = input("Welcome to sports.com, please select"
                          " \"L\" to Log In with your account or \"S\" to create an account: ")
        if selection.lower() == 's':
            register()
            answer = input("Would you like to Log In? Y/N? ")
            while answer:
                if answer.lower() == "y":
                    login()

                elif answer.lower() == "n":
                    exit()

                else:
                    answer = False
                    print("Invalid answer.")
                    continue
        elif selection.lower() == 'l':
            login()
            break
        else:
            print("Invalid answer.")
            continue


def register():
    username = input("Create your username (no more than 10 characters or less than 4.): ")
    while 10 < len(username) < 4:
        print('username cannot have more than 10 characters or less than 4.')
        username = input("Create your username (no more than 10 characters or less than 4.): ")
        break
    while username.isnumeric():
        print("username must contain at least one letter")
        username = input("Create your username (no more than 10 characters or less than 4.): ")
        break

    password = input("Create a password with letters and numbers: ")
    while len(password) < 6:
        print("Your password must contain more than 6 characters.")
        password = input("Create a password with letters and numbers: ")
        continue
    while password.isnumeric() or password.isalpha():
        print("Your password must contain both letters and numbers")
        password = input("Create a password with letters and numbers: ")
        continue

    login_credentials = open('C:\\Users\\hmarq\\Documents\\UsernameAndPassword.txt', 'a')
    login_credentials.write(f'{username},{password}\n')
    login_credentials.close()

    print("Account created successfully.")


def login() -> object:

    open('C:\\Users\\hmarq\\Documents\\UsernameAndPassword.txt', "r").readlines()

    username = input("Please enter your username: ").lower()
    while len(username) == 0:
        print("please enter a valid password")
        login()
    password = input("Please enter your password: ")

    with open('C:\\Users\\hmarq\\Documents\\UsernameAndPassword.txt', 'r') as login_credentials:
        lines = login_credentials.readlines()
        for line in lines:
            login_info, password_info = line.split(',')
            # print(login_info)
            # print(password_info)

            if username == login_info and password == password_info.strip():
                print("Authorized")
                authenticated = True
                return authenticated
    if username != login_info and password != password_info.strip():
        print("Incorrect credentials")
        authenticated = False
        return authenticated


def main():
    select_login_signup()


if __name__ == "__main__":
    main()
