from __future__ import division
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
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

def knn_jaccard(comment_train, test_comment, comment_solutions, k):
    # print "Performing k-Nearest Neighbor Solution with k = " + str(k)
    # print len(comment_train)
    # print len(comment_solutions)
    similarity_list = []
    index_list = []
    insult_list = []
    # first set up arrays of the proper sizes
    for i in range (0, k):
        similarity_list.append(0)
        index_list.append(-1)
        insult_list.append(-1)

    for i, comment in enumerate(comment_train):
        similarity = jaccard(comment, test_comment)

        for j in range (0, k):
            if similarity > similarity_list[j]:
                if j > 0:
                    sim_temp = similarity_list[j]
                    similarity_list[j - 1] = sim_temp
                    similarity_list[j] = similarity

                    index_temp = index_list[j]
                    index_list[j - 1] = index_temp
                    index_list[j] = i

                    insult_temp = insult_list[j]
                    insult_list[j - 1] = insult_temp
                    insult_list[j] = comment_solutions[i]
                else:
                    similarity_list[j] = similarity
                    index_list[j] = i
                    # print j, i, len(comment_solutions), len(comment_train)
                    insult_list[j] = comment_solutions[i]

    #print insult_list
    data = Counter(insult_list)
    is_insult = int(data.most_common(1)[0][0])
    return is_insult


def classify_jaccard(comment_train, test_comment, comment_solutions, threshold):
    # print "Performing Nearest Neighbor Solution with Jaccard Similarity"
    max_similarity = 0.0
    max_comment_index = -1
    for i, comment in enumerate(comment_train):
        similarity = jaccard(comment, test_comment)
        if similarity > max_similarity:
            max_similarity = similarity
            max_comment_index = i
        # print similarity

    # original error that still got 74% right
    # is_insult = 0
    # if max_similarity > threshold and max_comment_index != -1:
    #     is_insult = 1 # even though this is wrong, it still gets 75%????

    is_insult = int(comment_solutions[max_comment_index])

    return is_insult, max_comment_index

# Jaccard ratio can be found here:
# https://en.wikipedia.org/wiki/Jaccard_index
def jaccard(comment, test_comment):
    try:
        jac = len(set(comment).intersection(set(test_comment))) / float(len(set(comment).union(set(test_comment))))
    except ZeroDivisionError:
        return 0
    return jac