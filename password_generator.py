import string
import random

# Get Password length
minimum_password_length = int(6)
pw_lenght = input("Password Lenght?: ")
while True:
    try:
        pw_lenght = int(pw_lenght)
        if pw_lenght < minimum_password_length:
            print("You need more than " + str(minimum_password_length))
            pw_lenght = input("Please enter the Password Lenght again: ")
        else:
            break
    except:
        print("Please enter numbers only")
        pw_lenght = input("Please enter the Password Lenght again: ")

# Get Password characters types (Numbers, Letters, punctuation)
print("\nChoose the range of characters:")
print("to accept type y\n")

add_characters = input("Do you want the password to include Letters (y/n):")
add_punctuation = input(
    "Do you want the password to include punctuation (y/n):")
print("\n")

# Create Characters list
if add_characters == 'y' and add_punctuation == 'y':
    characters = list(string.ascii_letters +
                      string.digits + string.punctuation)
    print("Password will include Numbers, Letters and punctuation\n")
elif add_characters == 'y' and add_punctuation != 'y':
    characters = list(string.ascii_letters + string.digits)
    print("Password will include Numbers and Letters\n")
elif add_characters != 'y' and add_punctuation == 'y':
    characters = list(string.digits + string.punctuation)
    print("Password will include Numbers and punctuation\n")
else:
    characters = list(string.digits)
    print("Password will include Numbers only\n\0")

# shuffling the characters list
random.shuffle(characters)

# Generate the password


def generate_random_password():
    # picking random characters from the list
    password = []
    for i in range(pw_lenght):
        password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    # printing the list

    print('\033[1;96m')
    print("".join(password))


# invoking the function
generate_random_password()
