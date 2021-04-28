# Text Analysis 

I imported nltk and all the functions that I used during my analysis. 

    # Import libraries and functions for analysis.

    import nltk
    from nltk import word_tokenize
    from nltk import Text
    from nltk.stem import WordNetLemmatizer
    from nltk.probability import FreqDist
    from nltk.collocations import BigramCollocationFinder
    from nltk.metrics import BigramAssocMeasures

I imported my cleaned text file that was created at the end my clean_text.py file after the removal stopwords. 
   
    # Open and read the text file.

    f = open('cleaned_text.txt', 'r')
    raw = f.read()

I tokenized the text to split it into words for the computer to process. I used the text function to transform the tokens into a nltk text. I did this so I could use functions that are part of the ntlk library on my text. 

    # Text is transformed into tokens for computer to read.

    tokens = word_tokenize(raw)
    text = nltk.Text(tokens)

I added POS tags to the text. I also counted and found the most common tags out of curiousity. I mainly added tags so I could perform lemmatization. POS tags help indicate the purpose of the words in the text which in turn helps with lemmitization.
    
    # Find parts of speech in text. Define post tagging and count tags. Find most common tokens and their pos tag.

    tags = nltk.pos_tag(text)
    counts = Counter(tag for word, tag in tags)
    word_tag_fd = nltk.FreqDist(tags)
    word_tag_fd.most_common() 

I lemmatized my words because I wanted words of the same root to be grouped together when I looked at word frequency. For example, for "hospitals" to be transformed to "hospital", so they are counted together. I think this helped give a more accurate representation of the frequency of the most common words.

    # Lemmatize words.

    wordnet_lemmatizer = WordNetLemmatizer()
    total_lem = [wordnet_lemmatizer.lemmatize(t) for t in text]


I chose to find the most frequent words for each debate in order to investigate the rhetoric used by members of Parliament during each welfare debbates. Word frequency reveals the most common words, which can help indicate topics of discussion.
  
    # Find most frequent words in text. This will find the top 5 words.

    for t in total_lem:
        fdist = FreqDist(total_lem)
  
    print(fdist.most_common(5))

I chose to find the most frequent bigram collocations because I believed these results would reveal more about the topics of discussion within the debates. Collocations are two words that appear at a very high percentage compared to other words. I thought this analysis would support the findings of word frequency for indication of debates topics.

    # Finding bigram collocations in text. This will find the top 5 collocations.

    biagram_collocation = BigramCollocationFinder.from_words(total_lem)
    biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 5)