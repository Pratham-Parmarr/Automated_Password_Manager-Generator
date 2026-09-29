import string

def check_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
        
    has_upper = any(char in string.ascii_uppercase for char in password)
    has_number = any(char in string.digits for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    if has_upper:
        score += 1
    if has_number:
        score += 1
    if has_special:
        score += 1
        
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"