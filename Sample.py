import Auth
import twitterConfig
import twitterConfigAccessToken
from Twitter4Py3 import Pytwi

__author__ = 'y42sora'

"""
   This file is sample file
"""

if __name__ == "__main__":
    auth = Auth.TwitterOAuthHandler(twitterConfig.CONSUMER_KEY, twitterConfig.CONSUMER_SECRET)
    auth.setAccessToken(twitterConfigAccessToken.ACCESS_TOKEN, twitterConfigAccessToken.ACCESS_TOKEN_SECRET)
    rest = Pytwi.getRestAPI(auth)
    rest.publicTimeline()