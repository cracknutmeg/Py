import json
import difflib
from difflib import SequenceMatcher

data = json.load(open("dictionary.json"))

def translate(w):

    if w in data:
        return data[w]

    else:
        return "Such word doesn't exist. Check again!"

word = input("Type a word: ")

print(translate(word.lower()))
