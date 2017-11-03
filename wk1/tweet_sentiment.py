import sys
import json
import string
 

def readScores(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	#print scores.keys() # Print every (term, score) pair in the dictionary
	return scores

def readTweets(tweet_file):
	tweets = []
	for line in tweet_file:
		tweet = json.loads(line)
		if 'text' not in tweet.keys():
			continue
		tweets.append(tweet)
	return tweets

def calcSentiment(scores,tweets):
	for tweet in tweets:
		uniTweet = tweet['text'].encode('utf-8')
		tweetScore = 0
		for word in uniTweet.split(' '):
			if word in scores.keys():
				tweetScore +=scores[word] 
		print("%d" % tweetScore)			

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = readScores(sent_file)
    tweets = readTweets(tweet_file)

    calcSentiment(scores,tweets)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()