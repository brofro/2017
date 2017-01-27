from Utility.DomainModel.IProvider import IProvider

'''
The constants class which provides static helpers functions and constants
'''
class OpenWeatherApiConstants(IProvider):

    CurrentWeatherEndpoint = "weather"

    def __init__(self):
        super().__init__("OpenWeather", "http://api.openweathermap.org/data/2.5")
        self.ApiKey = ""

    def IsApiKeyValid(self):

        #TODO: Actually hit enpoint and check

        if self.ApiKey is "":
            self.PrintInvalidKey()
            return False

        return True

