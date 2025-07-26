fname = input("Enter File name to open: ")
try:
    fhand = open(fname)
except:
    print("File not found:", fname)
    exit()
if len(fname) < 1:
    print("File has no contents.")
word_count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        word = word.strip('.,!?()[]{}"\'')
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
total_words = sum(word_count.values())
print("Total words counted:", total_words)
print("Unique words found:", len(word_count))
print("Word frequency count:")
for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:1000]:
    print(word, count)

sorted_count=sorted(word_count.items(), key= lambda item: item[1], reverse=True)
print("\nTop 10 most frequent words in your file:")

for word, count in sorted_count[:10]:
    print(f"{word}: {count}")
fhand.close()
print("Word frequency count completed.")