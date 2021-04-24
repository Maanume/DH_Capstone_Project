# Text Analysis 

Import libraries and functions for analysis.
    
    import nltk
    from nltk import sent_tokenize, word_tokenize
    from nltk import Text
    from nltk.stem import WordNetLemmatizer
    from nltk.probability import FreqDist
    from nltk.collocations import BigramCollocationFinder
    from nltk.metrics import BigramAssocMeasures
    from collections import Counter

Open and read the text file.
   
    f = open('total_raw.txt', 'r')
    raw = f.read()

Text is transformed into tokens for computer to read.

    tokens = word_tokenize(raw)
    text = nltk.Text(tokens)

Find parts of speech in text. Define post tagging and count tags. Find most common tokens and their pos tag.
    
    tags = nltk.pos_tag(text)
    counts = Counter(tag for word, tag in tags)
    word_tag_fd = nltk.FreqDist(tags)
    word_tag_fd.most_common() 

Lemmatize words.

    wordnet_lemmatizer = WordNetLemmatizer()
    total_lem = [wordnet_lemmatizer.lemmatize(t) for t in text]

Find lexical density of text. Find total number of tokens and total number of unique tokens.

    len(total_lem)
    set(total_lem_)
    len(set(total_lem))

Find most frequent words in text. This will find the top 5 words.
  
    for t in total_lem:
        fdist = FreqDist(total_lem)
  
    print(fdist.most_common(5))

Finding bigram collocations in text. This will find the top 5 collocations.

    biagram_collocation = BigramCollocationFinder.from_words(total_lem)
    biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 5)