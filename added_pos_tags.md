# Adding POS Tags to Existing Pandas Dataframe
Import packages to identify and count parts of speech.

    import pandas as pd 
    import nltk
    from nltk import sent_tokenize, word_tokenize, pos_tag
    from collections import Counter

Insert and read the dataframe.
    
    df_debates = pd.read_csv('dataframe.csv')

Define function for counting nouns.

    def NounCount(x):
        nounCount = sum(1 for word, pos in pos_tag(word_tokenize(x)) if pos.startswith('NN'))
        return nounCount

Create a new column in dataframe for the the noun counts and apply to database.

    df_debates['noun_count'] = df_debates['text'].apply(NounCount)

Define unctions to count verbs, adjectives, adverbs and pronouns. Create new columns for each pos and apply to the dataframe.

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

Transform and save dataframe into a new csv file.

    df_debates.to_csv('df_debates.csv')