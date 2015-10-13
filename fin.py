import csv, operator, numpy, collections, itertools

def all_combinations(any_list, i):
    return itertools.chain.from_iterable(
        itertools.combinations(any_list, i))

def stringstonum(s1, s2):
    j = 0
    for i in range(0, len(s1)):
        if ((s1[i] == '1') and (s2[i] == '1')):
            j += 1
    return j

def stringstonum3(s1, s2, s3):
    j = 0
    for i in range(0, len(s1)):
        if ((s1[i] == '1') and (s2[i] == '1') and (s3[i] == '1')):
            j += 1
    return j

dictof1 = dict()

with open('market_data_transaction.txt','rb') as market:
    transactionreader = csv.reader(market, delimiter = ',')
    for row in transactionreader:
        for i in row:
            i = i.replace(" ", "")
            if i in dictof1:
                dictof1[i] += 1
            else:
                dictof1[i] = 1

listof1 = sorted(dictof1)

index = []
with open('market_data_binary.txt', 'rb') as binary:
    binreader = csv.reader(binary, delimiter = ' ')
    for row in binreader:
        index.append(row)

binstrings = ["" for i in range(0,11)]
for i in range(0,11):
    for j in range(0,5):
        binstrings[i] += str(index[j][i])

bindict = {}
for i in range(0,11):
    bindict[listof1[i]] = binstrings[i]
#print bindict

finaldict = {key: value for key, value in dictof1.items() if value >= 2.5}
freqlist1 = sorted(finaldict)
print freqlist1

listof2 = [list(l) for l in itertools.combinations(freqlist1,2)]
fin2 = []
for i in range(0, len(listof2)):
    if (stringstonum(bindict[listof2[i][0]], bindict[listof2[i][1]]) >= 2.5):
        fin2.append(listof2[i])

print fin2

listof3 = [list(l) for l in itertools.combinations(freqlist1,3)]
fin3 = []
for i in range(0, len(listof3)):
    if (stringstonum3(bindict[listof3[i][0]], bindict[listof3[i][1]], bindict[listof3[i][2]]) >= 2.5):
        fin3.append(listof3[i])

print fin3
