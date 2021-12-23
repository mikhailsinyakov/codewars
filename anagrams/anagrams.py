def anagrams(word, words):
    return [w for w in words if sorted(list(w)) == sorted(list(word))]
