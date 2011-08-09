__author__ = 'y42sora'

import urllib.request

import Error


def getMethod(url, auth=None, requireAuth=False):
    if requireAuth :
        if not auth :
            raise Error.PyTwiError('Auth required!')


    req = urllib.request.urlopen(url)
    print(req.read())

        