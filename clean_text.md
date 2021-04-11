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