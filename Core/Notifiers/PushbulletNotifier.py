#The notfier which sends to pushbullet
from Utility.Communication.HttpRequestHelper import GetHelper


def PushbulletNotifier(**kwargs):
    print "PushbulletNotifier sending data %s " % (kwargs.get("weatherData"))
    GetHelper(kwargs.get('endpoint'))