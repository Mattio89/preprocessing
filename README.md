# rmv-stopwords.py

Uses the [Natural Language ToolKit (NLTK)](http://www.nltk.org/) to prepare the data for topic modeling. Data is a txt file with one tweet per line (hashtags were already removed via OpenRefine). Filters according to the default dictionary to exclude commonly overrepresented words like "I", "the", and "and". Output is another textfile. Some topic models will accept the filtered text file, or it can be broken up using ...

# Split-Into-Many.py
[MALLET](http://mallet.cs.umass.edu/) input takes a directory of text files. This script splits the entire data set into .txt files that can be added to MALLET. Usefully, the filenames were what I used to cross reference the topic model data back onto the original file in the csv using graph_tweets.py and find_tweets.py in [visualization](https://github.com/Mattio89/visualization.git)