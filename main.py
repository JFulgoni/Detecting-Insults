from __future__ import division
import data_helper
import comment_helper

__author__ = 'johnfulgoni'

def check(insult_solutions, insult_test):
    print "Number of test comments: ", len(insult_test)
    print "Number of solution comments: ", len(insult_solutions)

    number_correct = 0
    #number_matches = 0
    for i in range (0, len(insult_test)):
        if i < 5:
            print insult_solutions[i], insult_test[i]

        # print type(insult_solutions[i])
        # print type(insult_test[i])
        # if insult_solutions[i] == 0:
        #     print 'derp'
        #     break
        if int(insult_solutions[i]) == insult_test[i]:
            # print "In here"
            number_correct += 1

    #print "Number matches: ", number_matches
    print "Number correct: ", number_correct
    print "Percentage correct: ", (number_correct/len(insult_test))

def main():
    print "Reading in Training Data..."
    insult_train, date_train, comment_train = data_helper.get_train()

    # print insult_train[0], date_train[0], comment_train[0]
    print "Processing Training Comments..."
    comment_train_processed = comment_helper.process_comments(comment_train)
    # for i in range (0, 5):
    #     print insult_train[i], comment_train_processed[i]

    print "Reading in Test Data with Solutions..."
    insult_test_solutions, date_test, comment_test = data_helper.get_test_with_solutions()
    print "Processing Testing Comments..."
    comment_test_processed = comment_helper.process_comments(comment_test)

    print "Classifying Test Comments..."
    insult_check = []
    for i, test_comment in enumerate(comment_test_processed):
        is_insult, closest_insult = comment_helper.classify_comment(comment_train_processed, test_comment, 0.75)
        insult_check.append(is_insult)
        # if is_insult:
        #     print "Original Tweet: ", comment_test[i]
        #     print "Is Insult? ", is_insult
        #     print "Closest Sentence: ", comment_train[closest_insult]
        #     break

    # print "Reading in Test Data..."
    # insult_test, date_test, comment_test = data_helper.get_test()
    # print "Processing Testing Comments..."
    # comment_test_processed = comment_helper.process_comments(comment_test)

    print "Checking Solutions..."
    check(insult_test_solutions, insult_check)

if __name__=="__main__":
    main()