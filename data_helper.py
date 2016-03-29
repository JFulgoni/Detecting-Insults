__author__ = 'johnfulgoni'
# This class gets all the data from data files and can send it to other parts of the code

import csv

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


# this method is really just for testing
# we'll use the other get data methods from our main file to actually run the code
def main():
    insult_list = []
    date_list = []
    comment_list = []
    filename = 'Data/train.csv'
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        counter = 0
        for row in csvreader:
            if counter < 102 and counter > 0:
                insult_list.append(row[0])
                date_list.append(row[1])
                comment_list.append(row[2])
                if counter == 1:
                    print row
            counter += 1
            #print row
    csvfile.close()
    print "Results:"
    print insult_list[0], date_list[0], comment_list[0]

if __name__=="__main__":
    main()