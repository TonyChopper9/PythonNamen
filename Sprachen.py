import re

def text_interpretation(text):

    text_split = text.split()
    #Teilt den Text an den Leerzeichen
    #!Zeilenumbruch und tab fehlen noch!
    #(vielleicht raw input)

    txtRegex = re.compile(r'[A-Z][a-z]+')
    _namen = list(filter(txtRegex.match, text_split))
    #Sammelt alle Namen in _namen

    text_noname = set(text_split) - set(_namen)
    #Entfernt die Namen aus dem Text

    #text_noname = list(filter(_namen, text_split))
    #text_noname = list(filter(lambda x: x not in txtRegex.match, text_split))
    #text_noname = (x for x in text_split and x not in _namen)

    return text_noname

def buchstaben_lesen(wlist):

    dictionary = {'a': 0}
    #Initialisierung des Wörterbuchs

    for wort in wlist:
        #Einzelne Worte aus Liste lösen

        for x in wort:
            #Buchstaben aus Wort lösen

            if dictionary.get(x) == None:
                #Falls noch kein Eintrag zum Buchstaben besteht

                dictionary[x] = 1

            else:
                #Eintrag existiert schon

                dictionary[x] += 1  
                #Eintrag inkrementieren

    for x in dictionary:
        return(dictionary)

print()
#print(text_interpretation(input("Testtext: \n")))
print(buchstaben_lesen(text_interpretation(input("Testtext: \n"))))







