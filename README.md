# Detecting-Insults
## John Fulgoni - 29 March 2016

Attempting a challenge from Kaggle.

The goal is to make a one-class classifier to determine if certain tweets are insults.
One of the hints given is that the classification tends to overfit.

This first run was actually wrong! I made the mistake of saying if the similarity was over the threshold, it was correct.
Somehow it still got 74% correct.

Number correct: 1974 / 2647
Percentage correct: 74.5749905553
Time taken to classify: 1.0:47.6741778851
Total time: 1.0:54.8430130482

With it actually fixed, it does much worse:

Number correct:  668 / 2647
Percentage correct:  25.2361163581
Time taken to classify: 1.0:44.8308780193
Total time: 1.0:51.5207140446

kNN of 3:
Number correct:  1948 / 2647
Percentage correct:  73.5927465055
Time taken to classify: 1.0:53.6695609093
Total time: 2.0:0.29797911644

kNN of 5: (Best so far)
Number correct:  2006 / 2647
Percentage correct:  75.783906309
Time taken to classify: 1.0:56.0384778976
Total time: 2.0:2.66123795509

Current state: tried to remove threshold component from classify_jaccard, now it's getting 0 right. So something is up...