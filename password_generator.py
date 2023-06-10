import string

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

# TODO shuffling the characters
# TODO Generate the password
