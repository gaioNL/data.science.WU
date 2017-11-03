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
	
	newWords={}

	for tweet in tweets:
		#1st calc the tweet sentiment
		tweetScore = 0
		uniTweet = tweet['text'].encode('utf-8')
		for word in uniTweet.split(' '):
			#uniWord = word.encode('utf-8')
			if word in scores.keys():
				tweetScore +=scores[word]
		#2nd assign the sentiment to new words	
		for word in uniTweet.split(' '):
			if word not in scores.keys():
				newWord = newWords.get(word)
				if newWord == None:
					#if it is a new word, add it
					newWords[word]=[1,tweetScore]
				else:
					#if it an existing word, add the tweet sentiment, accounting for both positive & negative tweets
					newWords[word]=[ newWord[0]+1, newWord[1] + tweetScore]
	#average the word scores
	for newWord in newWords:
		#print unicode(newWord).encode('utf-8')#+ " " + newWords[newWord][1]/newWords[newWord][0]
		print("%s %.3f" % ( newWord,newWords[newWord][1]/float(newWords[newWord][0])))		

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