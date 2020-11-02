#You are given a hexadecimal-encoded string that has been XOR'd against a single char.

#Decrypt the message. For example, given the string:

#7a 57 5e 5e 5d 12 455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f
#You should be able to decrypt it and get:

#Hello world from Daily Coding Problem


def find_char():
    h1 = 0x7A
    h2 = 0x57
    h3 = 0x5E
    h4 = 0X5D
    h5 = 0x12

    c1 = ord('H')
    c2 = ord('e')
    c3 = ord('l')
    c4 = ord('o')
    c5 = ord(' ')

    n = 0
    while n < 128:
        if n ^ h1 == c1 and n ^ h2 == c2 and n ^ h3 == c3 and n ^ h4 == c4 and n ^ h5 == c5:
            return n
        n = n + 1

    return -1

def get_decrypted_value(hex_char, encryption_char):
    hex_char = "0X" + hex_char
    int_value = int(hex_char, 16)
    decrypted_int = int_value ^ encryption_char
    return chr(decrypted_int)

def decrypt(encrypted_str, encryption_char):

    current_char = ""
    decrypted_string = ""
    for c in encrypted_str:
        if len(current_char) == 2:
            decrypted_string = decrypted_string + get_decrypted_value(current_char, encryption_char)
            current_char = ""
        current_char = current_char + c

    decrypted_string = decrypted_string + get_decrypted_value(current_char, encryption_char)
    return decrypted_string

c = find_char()
print(c)
print(chr(c))

decrypted_str = decrypt("7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f", c)
print(decrypted_str)
