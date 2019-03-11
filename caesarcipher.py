


"""
Encrypt a string with a simple code using a shift cipher.
Encode the characters in the character set given.

http://scienceblogs.com/goodmath/2008/08/11/rotating-ciphers/

"""

CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ,.\'\"?!'



def encrypt(m, k):
    """encrypt string m with key k using caesar cipher based on position in CHARSET"""
    # use accumulator pattern and build up result encrypting each char
    result_so_far = ''
    # for each char in the string to encrypt
    for c in m:   # with each char:
        # find the pos in the char set, and if the char is in the set...
        cPos = CHARSET.find(c)
        c_is_in_string = cPos != -1
        if c_is_in_string:
            # add the key to the position, rotate around if it overflows...
            encryptedPos = (cPos + k) % len(CHARSET)
            # find the char at the new position and add it to the result so far
            encryptedChar = CHARSET[encryptedPos]
            result_so_far = result_so_far + encryptedChar
    return result_so_far


def decrypt(m,k):
    """decrypt string m with key k using caesar cipher based on position in CHARSET"""
    result_so_far = ''
    for c in m:
        cPos = CHARSET.find(c)
        c_is_in_string = cPos != -1
        if c_is_in_string:
            encryptedPos = (cPos - k) % len(CHARSET)
            encryptedChar = CHARSET[encryptedPos]
            result_so_far = result_so_far + encryptedChar
    return result_so_far


def main():
    mode = input("Encrypt or Decrypt?  [e/d] ")
    message = input("Enter message ")
    key = int(input("Enter key (an integer) "))
    if mode == 'e':
        encryptedMessage = encrypt(message, key)
        print("Encrypted message is:\n", "'" + encryptedMessage + "'")
        # note the \n inserts a new line into the string
    else:
        decryptedMessage = decrypt(message, key)
        print("Decrypted message is:\n", "'" + decryptedMessage + "'")

main()

"""
Encrypt or Decrypt?  [e/d]e
Enter messageHello there friend, how are you?
Enter key (an integer)10
Encrypted message is:
 RovvyF3ro1oFp1soxnGFry6Fk1oF8y4

Process finished with exit code 0
"""
