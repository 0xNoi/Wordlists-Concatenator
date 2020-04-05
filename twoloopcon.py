#Created by @ozancetin > original repo github
#**********************ATTENTION**************************
#DO NOT TRY TO COMBINE MASSIVE WORDLISTS TOGETHER! 
#IF YOU TRY TO MAKE OVER THAN 50.000.000 WORDS WORDLIST, NOT RECOMMEND THIS SCRIPT
#pip install more-itertools 
#AND USE wordcon.py MUCH FASTER THAN THIS!
#ONLY 2 WORDLISTS CAN CONCATENATE!

import sys
import time

def twoloop_concatenator():
    start_time = time.time()
    ## create lists using square brackets
    wordlist1=[]
    wordlist2=[]
    w1 = open(sys.argv[1],'r')
    for line in w1:
	   wordlist1.append(line.strip())
    w2 = open(sys.argv[2],'r')
    for line2 in w2:
	   wordlist2.append(line2.strip())

    ## create a new empty list
    concatenated_words=[]

    ## first for loop: one iteration per item in wordlist1
    for i in range(len(wordlist1)):
        ## word with index i of wordlist1 (square brackets for indexing)
        word1=wordlist1[i]
        ## second for loop: one iteration per item in wordlist2
        for j in range(len(wordlist2)):
            word2=wordlist2[j]
            ## append concatenated words to the initially empty list
            concatenated_words.append(word1+word2)

    file = open("merged.txt", "w")
    ## iterate over the list of concatenated words, and write each item in a merged.txt
    for k in range(len(concatenated_words)):
        file.write(concatenated_words[k])
        file.write("\n")        
    file.close()

    print("Process Completed!\nFinished in: %s seconds\nCheck merged.txt" % (time.time() - start_time))


if __name__ == '__main__':
    try:
        twoloop_concatenator()
    except:
        print("Usage:\npython twoloopcon.py wordlist1.txt wordlist2.txt")