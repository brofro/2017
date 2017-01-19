from urllib import request
from urllib.parse import urlencode

'''
The set of REST helpers to communicate with external services
'''

#Sends an HTTP GET with optional queryString arguements to the provided url
def GetHelper(url, **kwargs):
    print("GET request to %s sent" % url)

    #Append query string
    if kwargs.get('queryString') is not None:
        queryString = urlencode(kwargs.get('queryString'))
        url += "?%s" % queryString

    response = request.urlopen(url)
    return response