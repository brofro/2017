from Core.Services.Abstract.ServiceBase import ServiceBase
from abc import ABCMeta

from Utility.Communication.HttpRequestHelper import GetHelper
from Utility.DomainModel.OpenWeatherAPI.GetCurrentWeatherResponse import GetCurrentWeatherResponse
from Utility.DomainModel.OpenWeatherAPI.OpenWeatherApiConstants import OpenWeatherApiConstants

'''
The distinct WeatherService which uses the provider to retrieve various kinds of data
'''
class WeatherService(ServiceBase):
    __metaclass__ = ABCMeta

    def __init__(self, handler, notifiers, **kwargs):
        super().__init__(handler, notifiers, OpenWeatherApiConstants, **kwargs)

    def Start(self):
        print("Starting: %s :: %s\n" % (self.Name, self.Endpoint))

        if not self.IsApiKeyValid():
            return

        data = self.GetData()

        for handler in self.Handlers:
            handler(self.Notifiers, weatherData=data, endpoint=self.Endpoint)

    def Stop(self):
        print ("\nStopping: %s" % self.Name)

    def GetData(self):
        #TODO Find a way to import city.list.json from http://bulk.openweathermap.org/sample/

        query = {'q':'Oakland', 'appid': self.Provider.ApiKey}

        route = self.Provider.GetRoute(OpenWeatherApiConstants.CurrentWeatherEndpoint)
        response = GetHelper(route, queryString=query)
        return GetCurrentWeatherResponse(response.read())

