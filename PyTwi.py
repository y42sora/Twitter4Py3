"""
   Copyright [2011] [y42sora]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
__author__ = 'y42sora'

import Auth
import Rest
import twitterConfig
import twitterConfigAccessToken

class Pytwi(object):
    """
    Twitter Api
    """

    def __init__(self):
        pass

    def getRestAPI(self, auth=None):
        return Rest.REST(auth)
    


if __name__ == "__main__":
    auth = Auth.TwitterOAuthHandler(twitterConfig.CONSUMER_KEY, twitterConfig.CONSUMER_SECRET)
    auth.setAccessToken(twitterConfigAccessToken.ACCESS_TOKEN, twitterConfigAccessToken.ACCESS_TOKEN_SECRET)
    rest = Pytwi.getRestAPI(auth)
    rest.publicTimeline()