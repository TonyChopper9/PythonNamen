import re
import csv


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


def csv_merge(d):
    try:

        with open('letterdata.csv') as csvfile:
            ftg = {}

            nd = dict(filter(None, csv.reader(csvfile)))
            #liest file in dictionary nd

            for x in nd:
                if nd[x] is not '':
                    nd[x] = int(nd[x])
                    #handlet leere zellen und macht die str nummern zu int

                else:
                    continue

            for x in d:
                try:
                    ftg[x] = nd[x] + d[x]
                    #addiert alle zu ändernden zellen in ftg
                except:
                    ftg[x] = d[x]

            nd.update(ftg)
            #pusht die neuen zellen auf nd

            #print(ftg)
            return(nd)


    except:
        print('ERROR_LESEN')


def csv_speichern(d):
    #Komma geht noch nicht
    try:

        with open('letterdata.csv', 'w') as csvfile:

            [csvfile.write('{0},{1}\n'.format(key, value)) for key, value in d.items()]

    except:
        print("ERROR_SPEICHERN")



#csv_speichern(buchstaben_lesen(text_interpretation(input("Testtext: \n"))))
csv_speichern(csv_merge(buchstaben_lesen(text_interpretation(input("Testtext: \n")))))







#Fehlversuche Sammlung:
#fieldnames = ['letter', 'absolute_frequency']

            #writer = csv.writer(csvfile)
            #for letter, absolute_frequency in d.items():
            #writer.writerow(letter, absolute_frequency)

            #columns = ['lttr', 'absf', 'relf']
            #w = csv.DictWriter(csvfile, d.keys())
            #w.writerow(d)

#for row in csvfile:
             #   print(row)
              #  x, y = row
               # d[x] += y

#text_noname = list(filter(_namen, text_split))
    #text_noname = list(filter(lambda x: x not in txtRegex.match, text_split))
    #text_noname = (x for x in text_split and x not in _namen)




