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


try:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"File {file_name} not found")
    exit(1)


if not content.strip():
    print("File is empty")
    exit(0)

lower_content = content.lower()


clean_content = lower_content
for char in punctuation:
    clean_content = clean_content.replace(char, " ")

clean_content_words_raw = clean_content.split()

clean_content_words = [word for word in clean_content_words_raw if word not in stop_words]

clean_dict = {}
for word in clean_content_words:
    if word in clean_dict:
        clean_dict[word] += 1
    else:
        clean_dict[word] = 1


sorted_clean_dict = dict(sorted(clean_dict.items(), key=lambda item: item[1], reverse=True))

word_count = len(clean_content_words_raw)
unique_words = len(sorted_clean_dict)
top_30 = list(sorted_clean_dict.items())[:30]

cnt = Counter(clean_content_words)

print("Total words:", word_count)
print("Unique words:", unique_words)
print("Top 30:", top_30)
print()
print("Top 30 (Counter):", cnt.most_common(30))

