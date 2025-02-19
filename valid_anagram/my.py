from collections import Counter

def isAnagram(s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        if counter_s == counter_t:
            return True
        else:
            return False

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))