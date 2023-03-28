def encoder(password):
    encode_password = ""
    for num in password:  # iterates through each number in 8 digit password
        encode_int = (int(num) + 3) % 10  # adds 3 to each integer digit, returns a value 0-9 b/c of % 10
        encode_password += str(encode_int)  # converts the encoded integer value to string, added to encode_password
    return encode_password


def decoder(password):
    decoded_pswrd = ""
    for num in password:
        if int(num) >= 3:  # If num - 3 does not reach -1
            new_value = int(num) - 3
        elif int(num) < 3:  # If num - 3 is less than 0
            new_value = (int(num) + 10) - 3
        decoded_pswrd += str(new_value)
    return decoded_pswrd


if __name__ == "__main__":
    run_program = True
    encode_pass = None  # stores the encoded password for the decode function

    while run_program:
        # list of menu options
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_option = input("\nPlease enter an option: ")  # intakes user input corresponding to menu options

        if user_option == "1":
            org_pass = str(input("Please enter your password to encode: "))
            encode_pass = encoder(org_pass)  # converts original password to encoded password and stores in encode_pass
            print("Your password has been encoded and stored!\n")
        elif user_option == "2":
            decode_pass = decoder(encode_pass)
            print(f"The encoded password is {encode_pass}, and the original password is {decode_pass}.\n")
        elif user_option == "3":
            run_program = False
