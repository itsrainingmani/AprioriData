import csv, operator, numpy, collections, itertools

def all_combinations(any_list, i):
    return itertools.chain.from_iterable(
        itertools.combinations(any_list, i))

#Function to see if the items are present in length 2 itemset
def stringstonum(s1, s2):
    j = 0
    for i in range(0, len(s1)):
        if ((s1[i] == '1') and (s2[i] == '1')):
            j += 1
    return j

#Function to see if the items are present in length 3 itemset
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

listof1 = sorted(dictof1)

index = []
with open('gene_data_binary.txt', 'rb') as bina:
    for line in bina:
        index.append(line.split())

binstrings = ["" for i in range(0,99)]
for i in range(0,99):
    for j in range(0,99):
        binstrings[i] += str(index[j][i])

finlist1 = []
for i in range(1,100):
    finlist1.append('gene_' + str(i))

bindict = {}
for i in range(0,99):
    bindict[finlist1[i]] = binstrings[i]

finaldict = {key: value for key, value in dictof1.items() if value >= 50}
freqlist1 = sorted(finaldict)

listof2 = [list(l) for l in itertools.combinations(freqlist1,2)]

fin2 = []
for i in range(0, len(listof2)):
    if (stringstonum(bindict[listof2[i][0]], bindict[listof2[i][1]]) >= 50):
        fin2.append(listof2[i])


listof3 = [list(l) for l in itertools.combinations(freqlist1,3)]

fin3 = []
for i in range(0, len(listof3)):
    if (stringstonum3(bindict[listof3[i][0]], bindict[listof3[i][1]], bindict[listof3[i][2]]) >= 50):
        fin3.append(listof3[i])

with open("itemset.txt","w+") as item:
    item.write("The Candidate itemset of length 1 is - " + str(listof1) + '\n')
    item.write("The Frequent itemset of length 1 is - " + str(freqlist1) + '\n')
    item.write("The Candidate itemset of length 2 is - " + str(listof2) + '\n')
    item.write("The Frequent itemset of length 2 is - " + str(fin2) + '\n')
    item.write("The Candidate itemset of length 3 is - " + str(listof3) + '\n')
    item.write("The Frequent itemset of length 3 is - " + str(fin3) + '\n')
