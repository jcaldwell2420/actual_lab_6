def encoder(password):
    encode_password = ""
    for num in password:  # iterates through each number in 8 digit password
        encode_int = (int(num) + 3) % 10  # adds 3 to each integer digit, returns a value 0-9 b/c of % 10
        encode_password += str(encode_int)  # converts the encoded integer value to string, added to encode_password
    return encode_password
