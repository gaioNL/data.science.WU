import os

from twitter import Api

# See assignment1.html instructions or README for how to get these credentials

api_key ="5KbvyiEaqHkya6sayoqj4c9Yw" #"<Enter api key>"
api_secret = "uV0Cu49zdiKmLcblpKfxMoMys8H1aEk2sf9Wf4tZ8HZjI9MKnf"#<Enter api secret>"
access_token_key = "22469231-nsyal3j5gleuXfJNy80rf93iHndcQxLHps6PW1I6f" #<Enter your access token key here>"
access_token_secret = "IiN8aE0pYIqBaKf5N7JlQc0NV0Iywr0RNC7VMyR9rGoNz" #"<Enter your access token secret here>"

# Since we're going to be using a streaming endpoint, there is no need to worry
# about rate limits.
api = Api(api_key,
          api_secret,
          access_token_key,
          access_token_secret)



def main():
  for line in api.GetSearch(term="seattle", count=1000):
    print (line)

if __name__ == '__main__':
    main()