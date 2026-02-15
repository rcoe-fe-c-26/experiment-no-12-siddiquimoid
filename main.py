length = int(input("Enter Length of Words: "))

with open("story.txt", "r") as file:
    text = file.read()

words = text.split()

result = set()

for word in words:
    word_lower = word.lower()
    if len(word_lower) == length:
        result.add(word_lower)

sorted_words = sorted(result)

print(f"Following Unique words of length {length} present: {sorted_words}")
