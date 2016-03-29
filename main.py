__author__ = 'johnfulgoni'

import data_helper
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string

en_stopwords = stopwords.words('english')
stemmer = SnowballStemmer('english')

def process_comments(comments):
    comment_list = []
    for comment in comments:
        # taking care of a lot of different factors when processing the comments
        # remove punctuation, lowercase, stopwords, stem words
        # turn into a list of lists
        comment = comment.strip(string.punctuation)
        comment = comment.lower()
        comment = comment.split()
        comment = remove_stopwords(comment)
        comment = stem_words(comment)
        comment_list.append(comment)
        # print comment
        # break
    return comment_list

def remove_stopwords(s):
    result = []
    for word in s:
        if word not in en_stopwords:
            result.append(word)
    return result

def stem_words(s):
    result = []
    for word in s:
        result.append(stemmer.stem(word))
    return result

def main():
    print "Reading in Training Data..."
    insult_train, date_train, comment_train = data_helper.get_train()

    #print insult_train[0], date_train[0], comment_train[0]
    print "Processing Training Comments..."
    comment_train_processed = process_comments(comment_train)
    for i in range (0, 5):
        print insult_train[i], comment_train_processed[i]

if __name__=="__main__":
    main()