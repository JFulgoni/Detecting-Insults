from __future__ import division
import datetime
import data_helper
import comment_helper


def is_correct_input(is_correct):
    return is_correct.lower() == "y" or is_correct.lower() == "n"


def validate_answer():
    is_correct = raw_input("Were we correct? [y/n]\n")
    if is_correct_input(is_correct):
        right_input = True
    else:
        right_input = False
    print datetime.datetime.now().strftime("%Y%m%d%H%M") + '\n'
    while not right_input:
        is_correct = raw_input("Please enter [y/n]\n")
        if is_correct_input(is_correct):
            right_input = True


def main():
    print "Reading in Training Data..."
    insult_train, date_train, comment_train = data_helper.get_train()

    # print insult_train[0], date_train[0], comment_train[0]
    print "Processing Training Comments..."
    comment_train_processed = comment_helper.process_comments(comment_train)

    cmd_input = ""
    while cmd_input != "quit":
        cmd_input = raw_input("What tweet would you like to test?\n")
        print cmd_input

        if cmd_input == "quit":
            continue

        is_insult, closest_insult = comment_helper.knn_jaccard(comment_train_processed, cmd_input, insult_train, 5)

        print is_insult
        if is_insult == 1:
            tweet_list = []
            for val in closest_insult:
                tweet_list.append(comment_train[val])
            print "Closest Tweets", tweet_list
        validate_answer()





if __name__ == "__main__":
    main()
