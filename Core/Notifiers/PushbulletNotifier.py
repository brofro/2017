from abc import ABCMeta

from Core.Notifiers.Abstract.INotifier import INotifier
from Utility.Communication.HttpRequestHelper import GetHelper

'''
The distinct notifier which sends data to Pushbullet API
'''
class PushbulletNotifier(INotifier):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__('PushbulletEndpoint')

    def Notify(self, **kwargs):
        weatherData = kwargs.get('weatherData')
        print ("PushbulletNotifier sending data %s to %s" % (weatherData.name + " has " + weatherData.weather[0]['main'], self.Destination))
        #GetHelper(self.Destination)