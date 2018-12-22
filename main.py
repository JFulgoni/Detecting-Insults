from __future__ import division
import data_helper
import comment_helper
import time

__author__ = 'johnfulgoni'

# checks the test with solutions, prints out total number correct as well as a percentage
def check(insult_solutions, insult_test):
    print "Number of test comments: ", len(insult_test)
    print "Number of solution comments: ", len(insult_solutions)

    number_correct = 0
    #number_matches = 0
    for i in range (0, len(insult_test)):
        # if i < 5:
        #     print insult_solutions[i], insult_test[i]

        # print type(insult_solutions[i])
        # print type(insult_test[i])
        # if insult_solutions[i] == 0:
        #     print 'derp'
        #     break
        if int(insult_solutions[i]) == insult_test[i]:
            # print "In here"
            number_correct += 1

    #print "Number matches: ", number_matches
    print "Number correct: ", number_correct, '/', len(insult_test)
    print "Percentage correct: ", (number_correct/len(insult_test) * 100)

# runs core functionality of the program
def main():
    t0 = time.time()
    print "Reading in Training Data..."
    insult_train, date_train, comment_train = data_helper.get_train()

    # print insult_train[0], date_train[0], comment_train[0]
    print "Processing Training Comments..."
    comment_train_processed = comment_helper.process_comments(comment_train)
    # for i in range (0, 5):
    #     print insult_train[i], comment_train_processed[i]

    print "Reading in Test Data with Solutions..."
    insult_test_solutions, date_test, comment_test = data_helper.get_test_with_solutions()
    # print len(insult_test_solutions), len(comment_test)
    print "Processing Testing Comments..."
    comment_test_processed = comment_helper.process_comments(comment_test)
    # print len(comment_test_processed)

    tA = time.time()
    print "Classifying Test Comments..."
    insult_check = []
    derp = True
    for i, test_comment in enumerate(comment_test_processed):
        # This one is Nearest Neighbor using the Jaccard Similarity
        is_insult, closest_insult = comment_helper.classify_jaccard(comment_train_processed, test_comment, insult_train,
                                                                    0.75)

        # This one also uses Jaccard, but does kNN instead of just nearest with a threshold
        # is_insult = comment_helper.knn_jaccard(comment_train_processed, test_comment, insult_train, 5)

        # if is_insult and derp:
        #     print test_comment, closest_insult
        #     derp = False

        # Add it to the list to be checked later
        insult_check.append(is_insult)
        # if i < 5:
        #      print is_insult, test_comment
        #      print insult_train[closest_insult]
        # else:
        #     break


        # if is_insult:
        #     print "Original Tweet: ", comment_test[i]
        #     print "Is Insult? ", is_insult
        #     print "Closest Sentence: ", comment_train[closest_insult]
        #     break

    # print "Reading in Test Data..."
    # insult_test, date_test, comment_test = data_helper.get_test()
    # print "Processing Testing Comments..."
    # comment_test_processed = comment_helper.process_comments(comment_test)

    tB = time.time()
    print "Checking Solutions..."
    check(insult_test_solutions, insult_check)

    # print "Insult train test: "
    # for x in range (0, 5):
    #     print insult_test_solutions[x], insult_check[x]

    tC = time.time()

    am, asec = divmod(tB-tA, 60)
    print 'Time taken to classify: ' + str(am) + ':' + str(asec)
    bm, bsec = divmod(tC-t0, 60)
    print 'Total time: ' + str(bm) + ":" + str(bsec)

if __name__=="__main__" :
    main()