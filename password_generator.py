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

# TODO Get Password characters types (Numbers, Letters, punctuation)
# TODO Create Characters list
# TODO shuffling the characters
# TODO Generate the password
