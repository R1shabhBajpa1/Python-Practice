# Count Word Frequency In A Dictionary
text = "hello world hello"
word_list = text.split()
word_freq = {}  
for word in word_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word Frequency:", word_freq)