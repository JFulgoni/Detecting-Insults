from __future__ import division
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string

__author__ = 'johnfulgoni'

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

def classify_comment(comment_train, test_comment, threshold):
    max_similarity = 0.0
    max_comment_index = -1
    for i, comment in enumerate(comment_train):
        similarity = jaccard(comment, test_comment)
        if similarity > max_similarity:
            max_similarity = similarity
            max_comment_index = i
        # print similarity
    is_insult = 0
    if max_similarity > threshold:
        is_insult = 1
    return is_insult, max_comment_index

# Jaccard ratio can be found here:
# https://en.wikipedia.org/wiki/Jaccard_index
def jaccard(comment, test_comment):
    try:
        jac = len(set(comment).intersection(set(test_comment))) / float(len(set(comment).union(set(test_comment))))
    except ZeroDivisionError:
        return 0
    return jac