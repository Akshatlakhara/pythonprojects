
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

print(data["smog"])
# print(data)


def translate(word):
    # get_close_matches ensures that if you wrote any word close to what you wanna search , it will automatically feed that word.

    # the if else search for the word or word in lower case and return it, else print not found.
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("is your word {}".format(
            get_close_matches(word, data.keys())[0]))
        decide = input("y for yes")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "not found"
    else:
        return "not found"


word = input("enter the word you want to search ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
