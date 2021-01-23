#shuffle.py

def encode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return shuffled_string

def decode_shuffle(message, secret):
    shuffled_string = do_shuffle(message, shuffle_axis(secret))
    return shuffled_string

def shuffle_axis(secret):
    number = 0
    for letter in secret:
        number += ord(letter)
    number += len(secret)
    return number

def do_shuffle(message, axis):
    message = list(message)
    message.reverse()
    def shift(seq, n):
        a = n % len(seq)
        return seq[-a:] + seq[:-a]
    
    message = shift(message, axis)
    return ''.join(message)
