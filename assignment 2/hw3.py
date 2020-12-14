word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc", "bye","yeb"]

# initialize a list
anagram_list = []
for word_1 in word_list: 
    for word_2 in word_list: 
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)


#another way
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)