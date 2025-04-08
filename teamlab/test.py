from typing import List
from collections import defaultdict

def most_duplicate(words: List[str]) -> str:
    dict = defaultdict(int)
    max_count = 0
    max_word = "zzzzzz"
    
    for word in words:
        dict[word] += 1
        if dict[word] > max_count:
            max_count = dict[word]
            if word < max_word:
                max_word = word

    return max_word


print(most_duplicate(["a", "b", "c", "a", "b", "a"])) # a