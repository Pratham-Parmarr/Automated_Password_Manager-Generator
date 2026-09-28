import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Base character set: lowercase letters
    char_pool = string.ascii_lowercase
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
        
    password = ""
    for _ in range(length):
        password += random.choice(char_pool)
        
    return password