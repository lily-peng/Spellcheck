# Lily Peng
# April 9, 2014
# Code for Twitch.tv's spellcheck problem: http://www.twitch.tv/problems/spellcheck
# This module will read a misspelled word from the user,
# then return the closest word from a locally stored .txt file

import re  # Regex
from string import ascii_lowercase


def is_vowel(letter):
    """ Checks if the inputted letter is a vowel. """
    if letter in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        return True
    return False

def make_pattern(original):
    """ This function generates a regex pattern specifically for this spellcheck from the original inputted string. """
    original = original.lower()
    pattern = ""
    prev = ""
    count = 1  # How many times a char appears in a row
    for index in range(len(original)+1):
        if index == len(original):  # Reached the empty after the string
            letter = ""
        else:
            letter = original[index:index+1]
        if letter == prev or (is_vowel(letter) and is_vowel(prev)):
            if count == 1:
                if is_vowel(letter):
                    pattern = pattern[:-7] + "(" + pattern[-7:]  # Insert parens before [aeiou]
            count = count + 1
        elif count > 1:
            if is_vowel(prev):
                pattern = pattern + ")"
            pattern = pattern + "{1," + str(count) + "}"
            count = 1
        if is_vowel(letter) and count == 1:
            pattern = pattern + "[aeiou]"
        elif count == 1:
            pattern = pattern + letter
        prev = letter

    return pattern


file_list = [(line.rstrip()) for line in open("words.txt")]  # Change this file to your dict file directory!
alphabet = ascii_lowercase
vowels = "eiou"
for i in range(len(vowels)):
    alphabet = alphabet.replace(vowels[i],"")

alphabet = list(alphabet)
lookup = [[]] * 22  # List of words that start with each letter
for word in file_list:
    if is_vowel(word[0]):
        if len(lookup[0]) == 0:
            lookup[0] = [word]
        else:
            lookup[0].append(word) 
    else:
        i = alphabet.index(word[0].lower())
        if len(lookup[i]) == 0:
            lookup[i] = [word]
        else:
            lookup[i].append(word)

while True:
    word_input = input(">")
    if word_input == "":
        print("NO SUGGESTION")
    else:
        pattern = make_pattern(word_input)
        word = word_input.lower()
        curr = []
        first_letter = word[0]
        if first_letter.isalpha():
            if is_vowel(first_letter):
                curr.extend(lookup[0])
            else:
                curr = lookup[alphabet.index(first_letter)]

        flag = False
        if curr == []:
            print("NO SUGGESTION")
            flag = True
        else:
            for result in curr:
                match = re.fullmatch(pattern, result, re.I)
                if match:
                    flag = True
                    print(result)
                    break
        if flag == False:
            print("NO SUGGESTION")
