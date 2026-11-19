phrase = "A man, a plan, a canal: Panama"

cleaned = ""
for ch in phrase.lower():
    if ch.isalnum():             # keep letters and digits only
        cleaned += ch

if cleaned == cleaned[::-1]:
    print(f'"{phrase}" is a palindrome')
else:
    print(f'"{phrase}" is not a palindrome')
