The code for the apriori algorithm is contained in one file, aptly named "apriori.py". It uses a function defined in the "itertools" library native to python, called "combinations". This generates all possible n-tuples of thge input list. I also used the binary transaction data to construct strings of 1's and 0's which I used to check if a certain itemset was frequent or not. I took the easy way out and instead of completely following the Apriori algorithm, I simply generated all n = 2, 3 itemsets and checked for minsup.

The code can be run by using the command - "python apriori.py" 
