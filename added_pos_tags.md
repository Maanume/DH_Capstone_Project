# Adding POS Tags to Existing Pandas Dataframe
ADD TEXT

    import pandas as pd 
    import nltk
    from nltk import sent_tokenize, word_tokenize, pos_tag
    from collections import Counter

ADD TEXT
    
     = pd.read_csv('total1.csv')
ADD TEXT

    def NounCount(x):
        nounCount = sum(1 for word, pos in pos_tag(word_tokenize(x)) if pos.startswith('NN'))
        return nounCount

ADD TEXT

    df_debates['noun_count'] = df_debates['text'].apply(NounCount)
ADD TEXT

    def VerbCount(x):
        verbCount = sum(1 for word, pos in pos_tag(word_tokenize(x)) if pos.startswith('VB'))
        return verbCount

    df_debates['verb_count'] = df_debates['text'].apply(VerbCount)

    def AdjectiveCount(x):
        adjectiveCount = sum(1 for word, pos in pos_tag(word_tokenize(x)) if pos.startswith('JJ'))
        return adjectiveCount

    df_debates['adj_count'] = df_debates['text'].apply(AdjectiveCount)

    def AdverbCount(x): 
        adverbCount = sum(1 for word, pos in pos_tag(word_tokenize(x)) if pos.startswith('RB'))
        return adverbCount

    df_debates['adverb_count'] = df_debates['text'].apply(AdverbCount)

    def PPCount(x): 
        ppCount = sum(1 for word, pos in pos_tag(word_tokenize(x)) if pos.startswith('PRP'))
        return ppCount

    df_debates['pronouns_count'] = df_debates['text'].apply(PPCount)

ADD TEXT

    df_debates.to_csv('total_ta.csv')