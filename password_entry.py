"""Heath Camp"""
MIN_LENGTH = 2
MAX_LENGTH = 6


def main():
    password = input("Enter Password: ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Enter Password: ")
    print("Your {} - character password is valid:".format(len(password)))
    print("Your password is: {}".format(convert_to_asterisks(password)))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    count_digit = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
    return True


def convert_to_asterisks(password):
    asterisks = len(password) * "*"
    return asterisks





main()

