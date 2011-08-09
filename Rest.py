__author__ = 'y42sora'

import HTTPGetMethod
import UrlListRestApi

class REST(object):

    auth = None
    def __init__(self, auth=None):
        self.auth = auth

    def homeTimeline(self):
        pass

    def publicTimeline(self):
        HTTPGetMethod.getMethod(UrlListRestApi.PUBLIC_TIMELINE)
