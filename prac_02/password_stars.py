MIN_LENGTH = 5

def main():
    """Main function to run the password program."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password from the user that meets the minimum length."""
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))

main()