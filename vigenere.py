# Decode a Vigenère cipher on the message
def decode_vigenere(message, secret):
    newmsg = ""
    for i in range(len(message)):
        if(message[i].isupper()):
            number = 65 + (ord(message[i]) - ord(secret[i%len(secret)])) % 26
            newmsg += chr(number)
        elif(message[i].islower()):
            number = 97 + (ord(message[i]) - ord(secret[i%len(secret)])) % 26
            newmsg += chr(number) 
        else:
            newmsg += message[i]
    return newmsg
