import sys
from functools import reduce
from collections import Counter

f=open(sys.argv[1])
contents=f.read().split()
print("Contents:\t")
print(*contents,sep=' ')

count_dict=Counter(contents)
print("\n",count_dict)

print("top 10 words with most occ in descending order:")
s=(sorted(count_dict.items(),key=lambda x:x[1],reverse=True))
print(s[:10])

wordlen=[len(i) for i,j in s[:10]]
print("Length of each word in list form is:",wordlen)

avg=(reduce(lambda x,y:x+y,wordlen))/len(wordlen)
print("Average:",avg)

sq_odd=[i*i for i in wordlen if i%2!=0]
print("square of odd numbers\t:",sq_odd)