class SentenceReverse:
    vowels=['a','e','i','o','u']
    sentence=''
    reverse=''
    vowelCount=0

    def __init__(self,sentence):
        self.sentence=sentence
    def reverseSentence(self):
        self.reverse=" ".join(reversed(self.sentence.split()))
        return self.reverse 
    def getvowelCount(self):
        self.vowelCount=sum(s in self.vowels for s in self.sentence.lower())
        return self.vowelCount
    # def getreverse(self):
        

item=[]

for i in range(3):
    reverser=SentenceReverse(input("Enter a Sentence"))
    item.append(reverser)
    print(reverser.reverse)

print("Descending order of number of vowels in string")
for i in sorted(item,key=lambda item:item.getvowelCount(),reverse=True):
    print(i.reverseSentence(),"->",i.getvowelCount())
