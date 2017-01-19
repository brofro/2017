class OpenWeatherApiConstants(object):

    Name = "OpenWeatherApi"

    ApiKey = "194081ece66e11a6bf8e2e9c1dda3a4d"

    MainRoute = "http://api.openweathermap.org/data/2.5"

    CurrentWeatherEndpoint = "weather"

    @staticmethod
    def GetRoute(endpoint):
        return  OpenWeatherApiConstants.MainRoute + "/" + endpoint


