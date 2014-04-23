# Lily Peng
# April 5, 2014
# Code for Twitch.tv's spellcheck problem: http://www.twitch.tv/problems/spellcheck
# This module will read a correctly spelled word from the user,
# then generate misspellings of the word for use in spellcheck.py

import random

def main():
    while True:
        original = input(">")
        output = ""
        word = original.lower()
        
        for letter in word:
            if letter in ("a", "e", "i", "o", "u"):
                r = random.randrange(5)
                if r == 0:
                    output = output + "a"
                    letter = "a"
                elif r == 1:
                    output = output + "e"
                    letter = "e"
                elif r == 2:
                    output = output + "i"
                    letter = "i"
                elif r == 3:
                    output = output + "o"
                    letter = "o"
                else:
                    output = output + "u"
                    letter = "u"
            else:
                output = output + letter

            # Repeats a letter 0-5 times    
            rr = random.randrange(6)
            rv = random.randrange(6)
            for i in range(rr):
                if letter in ("a", "e", "i", "o", "u"):
                    if rv == 0:
                        output = output + "a"
                    elif rv == 1:
                        output = output + "e"
                    elif rv == 2:
                        output = output + "i"
                    elif rv == 3:
                        output = output + "o"
                    else:
                        output = output + "u"
                else:
                    output = output + letter
                
        # Randomly sets each letter to upper or lowercase
        finished = ""
        for i, let in enumerate(output):
            rrr = random.randrange(2)
            if rrr == 0:
                finished = finished + output[i].upper()
            else:
                finished = finished + output[i].lower()
        print(finished)

main()
