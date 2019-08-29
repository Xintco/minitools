import random
import re
import sys
import unicodedata

trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308\u00F1'), None)

n=int(sys.argv[1])

words=[]
passl=[]
passw=""

with open("frases.txt") as f:
    
    for line in f:
        for word in re.findall(r'\w+', line):
            if len(word) <= 3:
                pass
            else:
                words.append(word)
#DEBUG print(words)
words=set(words)
words=list(words)
#DEBUG print(words)
l=len(words)


for x in range(n):
    word=words[random.randint(0,l)]
    #DEBUG#print(word)
    lw=len(word)
    uperand=(random.randint(0,lw-1))
    rdwo=word[int(len(word)/2):]+word[0:int(len(word)/2)]
    #DEBUG#print(rdwo)
    rdwo=rdwo[0:uperand]+rdwo[uperand].upper()+rdwo[uperand:]
    #DEBUG#print(rdwo)
    #DEBUG#print("###################")
    passl.append(rdwo)

sep=["!","@","$","&","%","=","#","0","1","2","3","4","5","6","7","8","9"]
secure_random = random.SystemRandom()

for word in range(len(passl)):
    passw=passw+secure_random.choice(sep)+passl[word]

passw=unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', passw).translate(trans_tab))
print(passw)



