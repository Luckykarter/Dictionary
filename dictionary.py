import json
import difflib #library for comparing text
import argparse

data = json.load(open("data/data.json"))

def get_translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    words = difflib.get_close_matches(word, data.keys(), n=5, cutoff=0.8)
    while words:
        word = words.pop(0)
        while True:
            decision = input("Do you mean %s? Y - yes, N - no\n" % word).lower()
            if decision == "y":
                return data[word]
            elif decision == "n":
                break
            else:
                continue

    return "The word does not exist. Please double-check"
def translate(word):
    result = get_translate(word)
    if isinstance(result, list):
        print('\n'.join(result))
    else:
        print(result)
def test():
    print("test")

parser = argparse.ArgumentParser(description='Dictionary')
parser.add_argument('-w', '--word', type=str, help='A word to describe')

args = parser.parse_args()
if not args.word:
    translate(input("Enter word: "))
else:
    translate(args.word)



