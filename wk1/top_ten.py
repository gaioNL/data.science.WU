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

def calcTags(tweets):
	
    allTags = {}

    for tweet in tweets:
		

        if tweet['entities']['hashtags'] == None:
            continue
    
        #get tweet hashtags
        tags = tweet['entities']['hashtags']
        for tag in tags:
            storedTag = allTags.get(tag['text'])
            if storedTag == None: # new tag
                allTags[tag['text']]=1
            else:
                allTags[tag['text']] +=1
    sortedTags =  sorted(allTags.items(), key=operator.itemgetter(1),reverse=True)

    maxTags = 10

    for tag in sortedTags:
        print tag[0] + " " + str(tag[1])
        maxTags -=1
        if maxTags==0:
            break

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
 
    tweet_file = open(sys.argv[1])
    tweets = readTweets(tweet_file)

    calcTags(tweets)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()