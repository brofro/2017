from Core.Services.Abstract.AbstractServiceBase import AbstractServiceBase
from abc import ABCMeta

class WeatherService(AbstractServiceBase):
    __metaclass__ = ABCMeta

    def __init__(self, name, endpoint):
        super(WeatherService, self).__init__(name, endpoint)

    def Start(self):
        print 'Starting Weather'

    def Stop(self):
        print 'Stopping'


