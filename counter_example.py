from collections import Counter

# Example 1: Simple word counting
print("=== Example 1: Simple word counting ===")
words = ["hello", "world", "hello", "python", "world", "hello"]
print(f"Original words list: {words}")

word_counts = Counter(words)
print(f"Counter result: {word_counts}")
print(f"Type: {type(word_counts)}")

# You can access counts like a dictionary
print(f"How many times 'hello' appears: {word_counts['hello']}")
print(f"How many times 'python' appears: {word_counts['python']}")

# Example 2: Most common words
print("\n=== Example 2: Most common words ===")
print(f"Most common 2 words: {word_counts.most_common(2)}")
print(f"Most common word: {word_counts.most_common(1)}")

# Example 3: Counter methods
print("\n=== Example 3: Counter methods ===")
print(f"All unique words: {list(word_counts.keys())}")
print(f"All counts: {list(word_counts.values())}")
print(f"Total words: {sum(word_counts.values())}")

# Example 4: Real text example
print("\n=== Example 4: Real text example ===")
text = "the quick brown fox jumps over the lazy dog the fox is quick"
words_from_text = text.split()
print(f"Text: {text}")
print(f"Words: {words_from_text}")

text_counter = Counter(words_from_text)
print(f"Word counts: {text_counter}")
print(f"Most common 3 words: {text_counter.most_common(3)}")
