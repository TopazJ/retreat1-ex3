#caesar.py

# Run a simple caesar cipher on the message
def encode_caesar(message, secret):
    offset = len(secret)
    offset %= 26
    return do_caesar(message, offset)

def decode_caesar(message, secret):
    return message #Real implementation in caesarfeat!

# Performs the caesar cipher operation
def do_caesar(message, offset):
    newmsg = ""
    for letter in message:
        if(letter.isupper()):
            number = ord(letter) + offset
            if(number >= (65+26)):
                number -= 26
            letter = chr(number)
        elif(letter.islower()):
            number = ord(letter) + offset
            if(number >= (97+26)):
                number -= 26
            letter = chr(number)
        newmsg += letter
    return newmsg