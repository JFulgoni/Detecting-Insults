__author__ = 'johnfulgoni'
# This class gets all the data from data files and can send it to other parts of the code

import csv
import datetime
import os


# returns the training set into three ordered lists
def get_train():
    insult_list = []
    date_list = []
    comment_list = []

    filename = 'Data/train.csv'

    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        counter = False
        for row in csvreader:
            if counter:
                insult_list.append(row[0])
                date_list.append(row[1])
                comment_list.append(row[2])
            counter = True
            #print row
    csvfile.close()
    # print "Results:"
    # print insult_list[0], date_list[0], comment_list[0]
    return insult_list, date_list, comment_list


def get_test():
    insult_list = []
    date_list = []
    comment_list = []

    filename = 'Data/test.csv'

    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        counter = False
        for row in csvreader:
            if counter:
                insult_list.append(row[0])
                date_list.append(row[1])
                comment_list.append(row[2])
            counter = True
    csvfile.close()
    return insult_list, date_list, comment_list


def get_test_with_solutions():
    insult_list = []
    date_list = []
    comment_list = []

    filename = 'Data/test_with_solutions.csv'

    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar = '"')
        counter = False
        for row in csvreader:
            if counter:
                insult_list.append(row[0])
                date_list.append(row[1])
                comment_list.append(row[2])
            counter = True
    csvfile.close()
    return insult_list, date_list, comment_list


def write_new_data(is_insult, tweet_date, tweet_text):
    filename = "Data/Generated/data_" + datetime.datetime.now().strftime("%Y%m%d")

    append_write = 'a' if os.path.exists(filename) else 'w'

    with open(filename, append_write) as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([is_insult, tweet_date, tweet_text])


# this method is really just for testing
# we'll use the other get data methods from our main file to actually run the code
def main():
    insult_list = []
    date_list = []
    comment_list = []
    filename = 'Data/test_with_solutions.csv'
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        counter = 0
        for row in csvreader:
            print row
            if counter < 102 and counter > 0:
                insult_list.append(row[0])
                date_list.append(row[1])
                comment_list.append(row[2])
                if counter == 3:
                    break
            counter += 1
            #print row
    csvfile.close()
    print "Results:"
    print insult_list[0], date_list[0], comment_list[0]

if __name__=="__main__":
    main()