def mask_password(text):
    masked = ""
    for char in text:
        masked += chr(ord(char) + 3)
    return masked

def unmask_password(masked_text):
    unmasked = ""
    for char in masked_text:
        unmasked += chr(ord(char) - 3)
    return unmasked