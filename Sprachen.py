import re

def text_interpretation(text):

    text_split = text.split()

    txtRegex = re.compile(r'[A-Z][a-z]+')
    _namen = list(filter(txtRegex.match, text_split))

    text_noname = set(text_split) - set(_namen)


    #text_noname = list(filter(_namen, text_split))

    #text_noname = list(filter(lambda x: x not in txtRegex.match, text_split))

    #text_noname = (x for x in text_split and x not in _namen)

    return text_noname

print()
print(text_interpretation(input("Testtext: \n")))






