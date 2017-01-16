#The notfier which sends to pushbullet
from abc import ABCMeta

from Core.Notifiers.Abstract.INotifier import INotifier
from Utility.Communication.HttpRequestHelper import GetHelper


class PushbulletNotifier(INotifier):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(PushbulletNotifier, self).__init__('PushbulletEndpoint')

    def Notify(self, **kwargs):
        print "PushbulletNotifier sending data %s to %s" % (kwargs.get('weatherData'), self.Destination)
        GetHelper(self.Destination)