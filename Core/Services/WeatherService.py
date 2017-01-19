'''
The distinct WeatherService
'''

from Core.Services.Abstract.ServiceBase import ServiceBase
from abc import ABCMeta

from Utility.Communication.HttpRequestHelper import GetHelper
from Utility.DomainModel.OpenWeatherAPI.GetCurrentWeatherResponse import GetCurrentWeatherResponse
from Utility.DomainModel.OpenWeatherAPI.OpenWeatherApiConstants import OpenWeatherApiConstants


class WeatherService(ServiceBase):
    __metaclass__ = ABCMeta

    def __init__(self, handler, notifiers, **kwargs):
        super().__init__(handler, notifiers, OpenWeatherApiConstants, **kwargs)

    def Start(self):
        print("Starting: %s :: %s\n" % (self.Name, self.Endpoint))
        data = self.GetData()
        for handler in self.Handlers:
            handler(self.Notifiers, weatherData=data, endpoint=self.Endpoint)

    def Stop(self):
        print ("\nStopping: %s" % self.Name)

    def GetData(self):
        query = {'q':'Oakland', 'appid': OpenWeatherApiConstants.ApiKey}
        route = OpenWeatherApiConstants.GetRoute(OpenWeatherApiConstants.CurrentWeatherEndpoint)
        response = GetHelper(route, queryString=query)
        return GetCurrentWeatherResponse(response.read())

