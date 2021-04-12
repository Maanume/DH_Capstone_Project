import nltk
from nltk import word_tokenize
from nltk import Text

f = open("rawtext.txt", 'r')
raw = f.read()

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

total_tokens = []
for t in text:
    if t.isalpha():
        t=t.lower()
        total_tokens.append(t)
    else:
        pass

from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))

sw_found = 0 

for t in total_tokens:
    if not t in stopset:
        appendFile = open('cleaned_si.txt', 'a')
        appendFile.write(" "+t)
        appendFile.close()
    else:
        sw_found +=1
