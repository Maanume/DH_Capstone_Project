# Cleaning and Normalizing Text

## Installation 
If you do not have anaconda or nltk installed on your computer follow the steps below.

For anaconda go to this [link](https://www.anaconda.com/products/individual), click download and then find the link that will work for your specific system. 

For nltk enter this line in Bash:

    pip install --user -U nltk

Test installation by typing:
    
    python

then
    
    import nltk

## Usage
I import nltk and these two functions because I use them to tokenize my text. I put them at the beginning at the script so that if I need to reference them they are imported first. 
   
    # To start insert the below text in Bash
    import nltk

    # These three lines import the Natural Language Toolkit (nltk) and import to other functions needed for cleaning.

    from nltk import word_tokenize
    from nltk import Text

I import my text file with my raw text so that I can clean and noramalize the text in preparation for analysis.

    #Next we need to import the text file we wish to clean.
    
    f = open('rawtext.txt', 'r')
    raw = f.read()

I chose to tokenize by word versus sentence because I wanted to focus on my analysis on words and not whole sentences. 
    
    # This turns the the raw text into a list of tokens. Then we turn this list into a NLTK text.

    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

I removed punctuation and changes all letters to lowercase to normalize the text. I chose to do this cleaning because my objective is focused on words and not punctuation. I also needed all my letters lowercase in order to have the same words be counted together. For example, without lowering 'Hospital' and 'hosiptal' would've been counted as seperate words. I chose to create a for-loop for this process because it seemed cleaner than writing each function out and defining a new variable.

    # Remove punctuation by only keeping tokens that are letters and then normalizing tokens to lowercase. This is a for-loop which loops thorugh the entire text going over every token.

    total_tokens = []
    for t in text:
        if t.isalpha():
            t=t.lower()
            total_tokens.append(t)
        else:
            pass

In order to find lexical density, I found the length of my text, which means the total number of words. I then grouped words together that are the same and found the length of that set in order to get the total number of unqiue words. Taking the total number of unique words and dividing by the total number of words give you the lexical density of the text. I chose to run this before removing stopwords in order to keep the lexical density accurate, as stopwords are part of the original text and should be counted.

    # Find lexical density of text. Find total number of tokens and total number of unique tokens.
    len(total_tokens)
    set(total_tokens)
    len(set(total_tokens))
    len(set(total_tokens))/len(total_tokens)

I imported the stopword list from NLTK. I chose this use the NLTK's enlgish stopword list because it contained all the words I wanted to remove. It also helped to maintain consistency as I used mostly tools from NLTK.
    
    # Import the stopwords from the nltk.corpus.
    
    from nltk.corpus import stopwords
    
    # Create a stopset list, we want the english version.
    stopset = set(stopwords.words('english'))

This counts how many stopwords the computer finds. I added this in order to know how many stopwords were removed from each text for comparison to the total word count I found above.
    
    # This is the stopwords found counter.
    sw_found = 0 
    
I created a for-loop to checks the words in the text and remove the stopwords and add those not on the stopword list to a new text file. I have the for-loop count how many stopwords it removes. I added the kept words to a new text file so I had a cleaned file for my analysis.
    
    # This is also a for-loop. If each word checked is not in the stopwords list then this will append the word to a new text file which I labeled cleaned_text.txt.

    for t in total_tokens:
    if not t in stopset:
        appendFile = open('cleaned_text.txt', 'a')
        appendFile.write(" "+t)
        appendFile.close()
     
    else:
        sw_found +=1

    len(sw_found)