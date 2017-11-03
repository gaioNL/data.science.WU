import sys
import json
import string

def readTweets(tweet_file):
	tweets = []
	for line in tweet_file:
		tweet = json.loads(line)
		if 'text' not in tweet.keys():
			continue
		tweets.append(tweet)
	return tweets

def calcTermFrequency(tweets):
	
	tweetWords={}

	totalWords = 0

	for tweet in tweets:

		uniTweet = tweet['text'].encode('utf-8')
	
		for word in uniTweet.split(' '):
			totalWords +=1#increase the total number of words
			tweetWord = tweetWords.get(word)
			if tweetWord == None:
				#if it is a new word, add it
				tweetWords[word]=[1]
			else:
				#if it an existing word, increase the occurence
				tweetWords[word]=[tweetWord[0]+1]
	
	#average the word scores
	for term in tweetWords:
		if term.strip() == "":
			pass
		else:
			print term.strip() + " %f" % (tweetWords[term][0]/float(totalWords))		

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    
    tweets = readTweets(tweet_file)

    calcTermFrequency(tweets)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()