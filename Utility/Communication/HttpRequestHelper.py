import urllib


def GetHelper(url, **kwargs):
    print("GET request to %s sent" % url)
    #response = urllib.request.urlopen(url)
    #return response


#a = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=194081ece66e11a6bf8e2e9c1dda3a4d"
#response = GetHelper(a).read()
#respObj = GetCurrentWeatherResponse(response)