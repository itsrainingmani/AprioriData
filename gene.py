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


with open('gene_data_transaction.txt','rb') as market:
    transactionreader = csv.reader(market, delimiter = ',')
    for row in transactionreader:
        for i in row:
            i = i.replace(" ", "")
            if i in dictof1:
                dictof1[i] += 1
            else:
                dictof1[i] = 1

print "The dict of 1 is - "
print dictof1

listof1 = sorted(dictof1)
print "The list of 1 is - "
print listof1

index = []
with open('gene_data_binary.txt', 'rb') as bina:
    for line in bina:
        index.append(line.split())
print "The index is - "
print index

binstrings = ["" for i in range(0,99)]
for i in range(0,99):
    for j in range(0,99):
        binstrings[i] += str(index[j][i])
#print binstrings

finlist1 = []
for i in range(1,100):
    finlist1.append('gene_' + str(i))

bindict = {}
for i in range(0,99):
    bindict[finlist1[i]] = binstrings[i]
print "The dict of binary strings - "
print bindict

finaldict = {key: value for key, value in dictof1.items() if value >= 50}
freqlist1 = sorted(finaldict)
print "Freq list of length 1 - "
print freqlist1

listof2 = [list(l) for l in itertools.combinations(freqlist1,2)]
print "Candidate itemset of L2 - "
print listof2
fin2 = []
for i in range(0, len(listof2)):
    if (stringstonum(bindict[listof2[i][0]], bindict[listof2[i][1]]) >= 50):
        fin2.append(listof2[i])

print "Frequnt itemset of L2 - "
print fin2

listof3 = [list(l) for l in itertools.combinations(freqlist1,3)]
print "Candidate itemset of L3 - "
print listof3

fin3 = []
for i in range(0, len(listof3)):
    if (stringstonum3(bindict[listof3[i][0]], bindict[listof3[i][1]], bindict[listof3[i][2]]) >= 50):
        fin3.append(listof3[i])

print "Freqeunt itemset of L3 - "
print fin3
