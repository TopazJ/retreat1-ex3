#shuffle.py

def encode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return ""

def shuffle_axis(secret):
    number = 0
    for letter in secret:
        number += ord(letter)
    number += len(secret)
    #number = number % len(message)
    print("axis of rotation for : " + secret + " is " + str(number))
    return number

def do_shuffle(message, axis):
    message = list(message)
    
    message.reverse()
    
    return ''.join(message)
