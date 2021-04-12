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

ADD TEXT
    
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

ADD TEXT
    
    total_tokens = []
    for t in text:
        if t.isalpha():
            t=t.lower()
            total_tokens.append(t)
        else:
            pass

ADD TEXT
    
    from nltk.corpus import stopwords

ADD TEXT
    
    stopset = set(stopwords.words('english'))

ADD TEXT
    
    sw_found = 0 
    
ADD TEXT   
    
    for t in total_tokens:
    if not t in stopset:
        appendFile = open('cleaned_si.txt', 'a')
        appendFile.write(" "+t)
        appendFile.close()
     
    else:
        sw_found +=1