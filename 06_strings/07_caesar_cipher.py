def shift_text(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif ch.islower():
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += ch         # keep spaces and punctuation
    return result

secret = shift_text("Hello, World!", 3)
print("Encrypted:", secret)
print("Decrypted:", shift_text(secret, -3))
