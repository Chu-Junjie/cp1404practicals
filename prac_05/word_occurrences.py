"""
Word Occurrences Counter
Count and display word occurrences in aligned columns.

Estimated time: 15 minutes
Actual time: 12 minutes
"""
text = input("Text: ")
words = text.split()
word_count = {}

# Count word frequencies (EAFP style)
for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1

# Find the longest word length for alignment
width = max(len(word) for word in word_count)

# Print sorted word counts with alignment
for word in sorted(word_count):
    print(f"{word:{width}} : {word_count[word]}")