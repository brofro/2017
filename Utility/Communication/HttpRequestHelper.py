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


def PostHelper(url, bodyJson, **kwargs):
    headers = {"content-type":"application/json"}

    #Check if we need to add access token to header
    if kwargs.get('accessToken') is not None:
        headers["Access-Token"] = kwargs.get('accessToken')

    #Reject for now if no access token
    else:
        print("POST request not provided with an accessToken")
        return None

    req = request.Request(url,
                          data = bodyJson,
                          headers = headers)

    response = request.urlopen(req)
    return response