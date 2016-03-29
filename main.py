from __future__ import division
import data_helper
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

#
def jaccard(comment, test_comment):
    return len(set(comment).intersection(set(test_comment))) / float(len(set(comment).union(set(test_comment))))

def main():
    print "Reading in Training Data..."
    insult_train, date_train, comment_train = data_helper.get_train()

    # print insult_train[0], date_train[0], comment_train[0]
    print "Processing Training Comments..."
    comment_train_processed = process_comments(comment_train)
    # for i in range (0, 5):
    #     print insult_train[i], comment_train_processed[i]

    print "Reading in Test Data..."
    insult_test, date_test, comment_test = data_helper.get_test()
    print "Processing Testing Comments..."
    comment_test_processed = process_comments(comment_test)

    print "Classifying Test Comments..."
    insult_check = []
    for i, test_comment in enumerate(comment_test_processed):
        is_insult, closest_insult = classify_comment(comment_train_processed, test_comment, 0.75)
        insult_check.append(is_insult)
        if is_insult:
            print "Original Tweet: ", comment_test[i]
            print "Is Insult? ", is_insult
            print "Closest Sentence: ", comment_train[closest_insult]
            break

if __name__=="__main__":
    main()