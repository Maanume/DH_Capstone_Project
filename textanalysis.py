
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk import Text
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from collections import Counter

f = open('total_raw.txt', 'r')
raw = f.read()

tokens = word_tokenize(raw)
text = nltk.Text(tokens)

tags = nltk.pos_tag(text)
counts = Counter(tag for word, tag in tags)
word_tag_fd = nltk.FreqDist(tags)
word_tag_fd.most_common() 

wordnet_lemmatizer = WordNetLemmatizer()
total_lem = [wordnet_lemmatizer.lemmatize(t) for t in text]

len(total_lem)
set(total_lem)
len(set(total_lem))
  
for t in total_lem:
    fdist = FreqDist(total_lem)
    
print(fdist.most_common(5))

biagram_collocation = BigramCollocationFinder.from_words(total_lem)
biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 5)