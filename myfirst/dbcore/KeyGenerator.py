import random

def generate_key(length):
    a = "qwrtyuiopadfghjlzcvbnm"
    b = "QWERTYUIOPASDFGHJKLZXCVBNM"
    c = "0123456789"
    d = a + b + c
    return "".join(random.sample(d, length))
