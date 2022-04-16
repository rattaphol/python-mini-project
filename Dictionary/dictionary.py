import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] 
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on working keys ")
        else:
            return("You have entered wrong input please enter just y or n")    
    else:
        print("You have entered wrong keys. Try again")
        

print("\n ================================= \n Welcome to Dictionary Query Program!\n =================================\n")
i = 0
while 1:
    i += 1 
    word = input("\nEnter the word ["+ str(i) +"] you want to search [zzz to exit]: ")
    word = word.lower()
    word = word.strip()
    if word == "zzz":
        break
    else:
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

print("\n ================================= \n Thank you hope to see you again!\n =================================\n")