word_to_count = {}
text = str(input("Text: "))
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
words = list(word_to_count.keys())
words.sort()
max_character = max(len(word) for word in list(word_to_count.keys()))
for word in words:
    print(f"{word:{max_character}} - {word_to_count[word]}")


