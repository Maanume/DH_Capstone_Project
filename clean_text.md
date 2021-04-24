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
To start insert the below text in Bash:

    import nltk
    from nltk import word_tokenize
    from nltk import Text

These three lines import the Natural Language Toolkit (nltk) and import to other functions needed for cleaning.

Next we need to import the text file we wish to clean.

    f = open('rawtext.txt', 'r')
    raw = f.read()

This turns the the raw text into a list of tokens. Then we turn this list into a NLTK text.
    
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

Remove punctuation by only keeping tokens that are letters and then normalizing tokens to lowercase. This is a for loop which loops thorugh the entire text. going over every token.
    
    total_tokens = []
    for t in text:
        if t.isalpha():
            t=t.lower()
            total_tokens.append(t)
        else:
            pass

Import the stopwords from the nltk.corpus.
    
    from nltk.corpus import stopwords

Create a stopset list, we want the english version.
    
    stopset = set(stopwords.words('english'))

THis is the stopwords found counter.
    
    sw_found = 0 
    
This is also a for loop. If each word checked is not in the stopwords list then this will append the word to a new text file which I labeled cleaned_text.txt.
    
    for t in total_tokens:
    if not t in stopset:
        appendFile = open('cleaned_text.txt', 'a')
        appendFile.write(" "+t)
        appendFile.close()
     
    else:
        sw_found +=1