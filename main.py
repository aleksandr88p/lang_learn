from collections import Counter

stop_words = {
    "a", "an", "the",
    "and", "or", "but",
    "to", "of", "in", "on", "at", "for", "from", "with",
    "is", "are", "was", "were", "be", "been",
    "i", "you", "he", "she", "it", "we", "they",
    "my", "your", "his", "her", "our", "their",
    "this", "that", "these", "those",
    "so", "as", "if", "then", "than",
}
punctuation = ".,!?;:-()[]{}\"“”—–…«»‹›"

file_name = "transcript.txt"

def read_file(filename: str) -> str:

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def normalize_content(content: str) -> str:
    lower_content = content.lower()
    clean_content = lower_content
    for char in punctuation:
        clean_content = clean_content.replace(char, " ")
    return clean_content

def remove_stop_words(words: list[str]) -> list[str]:
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words


try:
    content = read_file(filename=file_name)
except FileNotFoundError:
    print("File not found")
    exit(1)


if not content.strip():
    print("File is empty")
    exit(1)

clean_content = normalize_content(content)
words = clean_content.split()
filtered_words = remove_stop_words(words)
word_count = len(words)
unique_words = len(set(words))
cnt = Counter(filtered_words)
print("Total words:", word_count)
print("Unique words:", unique_words)
print()
print("Top 30 (Counter):", cnt.most_common(30))


