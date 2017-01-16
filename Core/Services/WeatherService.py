from Core.Services.Abstract.AbstractServiceBase import AbstractServiceBase
from abc import ABCMeta

class WeatherService(AbstractServiceBase):
    __metaclass__ = ABCMeta

    def __init__(self, handler, notifiers, **kwargs):
        super(WeatherService, self).__init__('WeatherService', 'WeatherEndpoint'
                                             , handler, notifiers, **kwargs)

    def Start(self):
        print "Starting: %s\nEndpoint: %s\n" % (self.Name, self.Endpoint)
        for handler in self.Handlers:
            handler(self.Notifiers, weatherData=self.HandlerArgs, endpoint=self.Endpoint)

    def Stop(self):
        print "Stopping: %s\n" % self.Name


