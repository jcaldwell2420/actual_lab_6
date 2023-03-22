def encoder(password):
    encode_password = ""
    for num in password:  # iterates through each number in 8 digit password
        encode_int = (int(num) + 3) % 10  # adds 3 to each integer digit, returns a value 0-9 b/c of % 10
        encode_password += str(encode_int)  # converts the encoded integer value to string, added to encode_password
    return encode_password

if __name__ == "__main__":
    run_program = True
    encode_pass = None  # stores the encoded password for the decode function

    while run_program:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
