text = "python makes programming simple and fun to learn"

word_count = 0
longest = ""
for word in text.split():
    word_count += 1
    if len(word) > len(longest):
        longest = word

print("Words:", word_count)
print("Longest word:", longest, f"({len(longest)} letters)")
print("Characters (no spaces):", len(text.replace(" ", "")))

# capitalize every word
titled = ""
for word in text.split():
    titled += word.capitalize() + " "
print(titled.strip())
print("-".join(text.split()))        # join words with a dash
