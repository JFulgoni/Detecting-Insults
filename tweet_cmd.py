from __future__ import division
import datetime
import data_helper
import comment_helper

correctness_map = {"1y": 1, "1n": 0, "0y": 0, "0n": 1}


def is_correct_input(is_correct):
    return is_correct.lower() == "y" or is_correct.lower() == "n"


def validate_answer(is_insult):
    is_correct = raw_input("Were we correct? [y/n]\n")
    while not is_correct_input(is_correct):
        is_correct = raw_input("Please enter [y/n]\n")
    return correctness_map[str(is_insult) + is_correct]


# This can be used to test an individual tweet at a time from the command line
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

        if is_insult:
            tweet_list = [comment_train[item] for item in closest_insult]
            print "Closest Tweets", tweet_list

        tweet_date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        data_helper.write_new_data(validate_answer(is_insult), tweet_date, cmd_input)


if __name__ == "__main__":
    main()
