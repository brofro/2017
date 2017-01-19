'''
The constants class which provides static helpers functions and constants
'''
class OpenWeatherApiConstants(object):

    #TODO Extract methodds into abstract class

    Name = "OpenWeatherApi"

    ApiKey = ""

    MainRoute = "http://api.openweathermap.org/data/2.5"

    CurrentWeatherEndpoint = "weather"

    @staticmethod
    def GetRoute(endpoint):
        return  OpenWeatherApiConstants.MainRoute + "/" + endpoint


