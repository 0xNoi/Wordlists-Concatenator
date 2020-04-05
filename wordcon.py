#Created by @ozancetin > original repo github
#DO NOT TRY TO COMBINE SUPER MASSIVE WORDLISTS TOGETHER!
#DO NOT FORGET:
#pip install more-itertools 

import itertools
import sys
import time

def wordlist_concatenator():
	start_time = time.time()
	wordlist1=[]
	wordlist2=[]
	wordlist3=[]
	
	w1 = open(sys.argv[1],'r')
	for line in w1:
		wordlist1.append(line.strip())
	w2 = open(sys.argv[2],'r')
	for line2 in w2:
		wordlist2.append(line2.strip())
	try:
		w3 = open(sys.argv[3],'r')
		for line3 in w3:
			wordlist3.append(line3.strip())
		result = ["".join(i) for i in itertools.product(wordlist1, wordlist2, wordlist3)]
	except:
		result = ["".join(i) for i in itertools.product(wordlist1, wordlist2)]

	file = open("merged.txt", "w") 
	file.write('\n'.join(result))
	file.close()
	print("Process Completed!\nFinished in: %s seconds\nCheck merged.txt" % (time.time() - start_time))

if __name__ == '__main__':
	try:
		wordlist_concatenator()
	except:
		print("Usage:\npython wordcon.py wordlist1.txt wordlist2.txt\npython wordcon.py wordlist1.txt wordlist2.txt wordlist3.txt ")
