import re
import csv


def text_interpretation(text):

    txtRegex = re.compile(r'[a-z] [A-Z][a-z]+')
    namenRegex = re.compile(r'[A-Z][a-z]+')
    #beide Regex patterns

    _namen = txtRegex.findall(text)
    #namen mit ende des Wortes davor

    l = len(_namen)
    neu_namen = [0]*l

    for i in range(0, l):
        neu_namen[i] = namenRegex.findall(_namen[i])[0]
        #neue liste mit nur den worten ohne das davor


    text_split = text.split()
    text_noname = set(text_split) - set(neu_namen)

    return text_noname


def buchstaben_lesen(wlist):

    dictionary = {'a': 0}
    #Initialisierung des Wörterbuchs

    for wort in wlist:
        #Einzelne Worte aus Liste lösen

        for x in wort:
            #Buchstaben aus Wort lösen

            if x == ',':
                continue
            else:
                pass

            if dictionary.get(x) == None:
                #Falls noch kein Eintrag zum Buchstaben besteht

                dictionary[x] = 1

            else:
                #Eintrag existiert schon

                dictionary[x] += 1
                #Eintrag inplementieren

    for x in dictionary:
        return(dictionary)


def csv_merge(d):
    try:

        try:
            with open('letterdata.csv','r') as nothing:
                pass
        except:
            with open('letterdata.csv', 'w+') as nothing:
                pass
        #existenzcheck

        with open('letterdata.csv') as csvfile:

            ftg = {}

            nd = dict(filter(None, csv.reader(csvfile)))
            #liest file in dictionary nd

            if nd is None:
                nd = {'a':0}
                #neues file

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

            try:
                del nd[',']
            except:
                pass


            #print(ftg)
            return(nd)


    except:
        print('ERROR_FILE_LESEN')


def csv_speichern(d):
    try:

        sum_d = 0
        rel_prob = {}
        all = []

        for i in d:
            sum_d += d[i]

        for x in d:
            rel_prob[x] = d[x] / sum_d


        with open('letterdata.csv', 'w') as csvfile:
            [csvfile.write('{0},{1}\n'.format(key, value)) for key, value in d.items()]

        #relative wahrscheinlichkeit file
        with open('letterdata.csv') as c:
            r = csv.reader(c)

            for item in r:
                item.append(rel_prob[item[0]])
                all.append(item)

        with open('relletterdata.csv', 'w') as outcsv:
            writer = csv.writer(outcsv, lineterminator = '\n')
            writer.writerows(all)


    except:
        print("ERROR_SPEICHERN")


def txt_lesen():
    try:

        with open('Datastring.txt', 'r')  as text_origin:
            return(text_origin.read())
    except:
        print("ERROR: Datei nicht vorhanden")


def __main__():

    csv_speichern(csv_merge(buchstaben_lesen(text_interpretation(txt_lesen()))))


__main__()


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




