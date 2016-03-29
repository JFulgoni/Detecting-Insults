__author__ = 'johnfulgoni'

import data_helper

def main():
    insult_train, date_train, comment_train = data_helper.get_train()

    print insult_train[0], date_train[0], comment_train[0]

if __name__=="__main__":
    main()