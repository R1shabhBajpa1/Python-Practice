# To Find Longest Word In String
text = "Find the longest word in this string"
words = text.split()
longest_word = ""   
for word in words:
    if len(word) > len(longest_word):
        longest_word = word 
print("Longest Word:", longest_word)