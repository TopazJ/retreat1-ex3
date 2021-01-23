# Uncomment these imports when you'd like to test:
#from caesar import encode_caesar, decode_caesar
#from shuffle import encode_shuffle, decode_shuffle
#from vigenere import encode_vigenere, decode_vigenere

# Main function
def run_test():
    while True:
        print("Enter 1 to encode a message, or 2 to decode a message")
        userinput = input()
        if(userinput == "1"):
            encode_test()
            break
        elif(userinput == "2"):
            decode_test()
            break

# If the user has decided to encode a message
def encode_test():
    print("Enter a message to encode:")
    message = input()
    print("Enter a secret to help encode your message:")
    secret = input()
    encoded_message = encode(message, secret)
    print("Encoded message: \n" + encoded_message)

# If the user has decided to decode a message
def decode_test():
    print("Enter a message to decode:")
    message = input()
    print("Enter a secret to help decode your message:")
    secret = input()
    decoded_message = decode(message, secret)
    print("Decoded message: \n" + decoded_message)

# Perform a set of encoding operations
# You may customize which set of operations you encode with
def encode(message, secret):
    return message 
    # Example:
    # return encode_caesar(encode_shuffle(message, secret), secret)

# Decode the message.
# You should use the encoding operations in reverse order with the same secret
def decode(message, secret):
    return message
    # Example:
    # return decode_shuffle(decode_caesar(message, secret), secret)

# Run a simple test
run_test()

#      _,---._
#    /'  ,`.  `\
#  /'`,,'   ;   )         thank you for participating w
# (_   ;  ,-,---'      ~~~~~~~ HACK YOUR LEARNING! ~~~~~~~~
#  (;;,,;/--'
#   \;;;/
#     /