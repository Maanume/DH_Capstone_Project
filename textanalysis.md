# Text Analysis 

Import of libraries
    
    import nltk
    from nltk import sent_tokenize, word_tokenize
    from nltk import Text
    from nltk.stem import WordNetLemmatizer
    from nltk.probability import FreqDist
    from nltk.collocations import BigramCollocationFinder
    from nltk.metrics import BigramAssocMeasures
    from collections import Counter

Opening and reading the file 
   
    f = open('total_raw.txt', 'r')
    raw = f.read()

Text is transformed into tokens for computer to read  

    tokens = word_tokenize(raw)
    text = nltk.Text(tokens)

Parts of speech tagging
    
    tags = nltk.pos_tag(text)
    counts = Counter(tag for word, tag in tags)
    word_tag_fd = nltk.FreqDist(tags)
    word_tag_fd.most_common() 

Lemmatizing words to find lexical density

    wordnet_lemmatizer = WordNetLemmatizer()
    total_lem = [wordnet_lemmatizer.lemmatize(t) for t in text]
    
    len(set(total_lem))

Most frequent words
  
    for t in total_lem:
        fdist = FreqDist(total_lem)
  
    print(fdist.most_common(25))

Finding biagrams 

    biagram_collocation = BigramCollocationFinder.from_words(total_lem)
    biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 5)