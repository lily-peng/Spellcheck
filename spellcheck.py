# Lily Peng
# April 5, 2014
# Code for Twitch.tv's spellcheck problem: http://www.twitch.tv/problems/spellcheck
# This module will read a misspelled word from the user,
# then return the closest word from a locally stored .txt file
# using a trie implementation.

vowels = ["a", "e", "i", "o", "u"]

def my_trie(words):
    """ My trie implementation """
    root = dict()
    for word in words:
        current_dict = root
        for raw_letter in word:
            letter = raw_letter.lower()
            current_dict = current_dict.setdefault(letter, {})
            current_dict["_self"] = letter
        current_dict = current_dict.setdefault("_end", words.index(word))
    return root

def is_vowel(letter):
    """ Checks if the inputted letter is a vowel. """
    if letter in vowels:
        return True
    return False

def iterate(curr, word, index, results):
    """ Performs the main search through the trie. """
    to_visit = []
    if index < len(word):
        letter = word[index]
        for key in curr.keys():  # For every child letter of curr
            exact_match = (key == letter)
            vowel_match = is_vowel(key) and is_vowel(letter)
            match = exact_match or vowel_match 
            if match:
                next_child = curr[key]
                if isinstance(next_child, dict):
                    for key2 in next_child.keys():  # For every child letter of next_child
                        if key2 == "_end":  # Reached the end of a word
                            if index == len(word)-1:
                                results.append(next_child[key2])
                to_visit.append(curr[key])  # Adding letters
				
        temp = curr.get("_self","")  # Previous letter, or curr letter
        vowel_matches = is_vowel(temp) and is_vowel(letter)
        if is_vowel(temp):
            for vowel in vowels:
                if not curr.get(vowel,"") == "":
                    break
        if letter == temp or (vowel_matches):
            if index == len(word)-1:  # Repeating letter at end of word
                results.append(curr.get("_end"))
            to_visit.append(curr) # Requeue itself
        while not to_visit == []:
            node = to_visit.pop(-1)
            iterate(node, word, index+1, results)

def search_results(root, word):
    """ Returns results from the trie search. """
    results = []
    iterate(root, word, 0, results)
    if len(results) == 0:
        return "NO SUGGESTIONS"
    else:
        for r in results:
            if word == file_list[r].lower():
                return file_list[r]
        return file_list[(results[0])]

print("Loading...")
file_list = [(line.rstrip()) for line in open('words.txt')]
trie = my_trie(file_list)
to_visit = []

while True:
    word = input(">")
    word = word.lower()
    index = 0
    curr = trie
    print(search_results(curr, word))
