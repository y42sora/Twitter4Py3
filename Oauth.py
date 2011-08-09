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

import base64
import urllib
import time
import random
import hmac
import binascii
import cgi


class OAuthConsumer(object):
    """
    This class have Consumer key and secret
    """
    key = None
    secret = None

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

class OauthToken(object):
    """
    This class have 
    """
    key = None
    secret = None
    callback = None

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret