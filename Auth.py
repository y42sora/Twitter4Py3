__author__ = 'y42sora'

import Oauth

class TwitterOAuthHandler(object):
    AUTHORIZATION_URL = 'http://api.twitter.com/oauth/authorize'
    AUTHENTICATE_URL  = 'http://api.twitter.com/oauth/authenticate'
    REQUEST_TOKEN_URL = 'http://api.twitter.com/oauth/request_token'
    ACCESS_TOKEN_URL  = 'http://api.twitter.com/oauth/access_token'

    consumer = None
    requestToken = None
    accessToken = None
    callback = None
    
    def __init__(self, consumerKey, consumerSecret, callback=None):
        self.consumer = Oauth.OAuthConsumer(consumerKey, consumerSecret)
        self.requestToken = None
        self.accessToken = None
        self.callback = callback
        
    def setAccessToken(self, key, secret):
        self.accessToken = Oauth.OauthToken(key, secret)
        


