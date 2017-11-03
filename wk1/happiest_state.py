import sys
import json

import string
import operator
 
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

def calcHappiness(scores,tweets):
	
    tweetStates = {}

    for tweet in tweets:
		
        #use Place key to determine location
        if 'place' not in tweet.keys() or tweet['place'] == None:
            continue
        #process just tweets from US
        if tweet['place']['country_code'] != "US":
            continue
        #get tweet state
        state = tweet['place']['full_name'][-2:]
        tState = tweetStates.get(state)
        if tState == None:
            tweetStates[state]=0

        #get tweet text & state
        uniTweet = tweet['text'].encode('utf-8')
        
        #calc state happiness
        for word in uniTweet.split(' '):
            if word in scores.keys():
                tweetStates[state] +=scores[word] 

    sortedStates =  sorted(tweetStates.items(), key=operator.itemgetter(1),reverse=True)

    print(sortedStates[0][0])

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = readScores(sent_file)
    tweets = readTweets(tweet_file)

    calcHappiness(scores,tweets)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()