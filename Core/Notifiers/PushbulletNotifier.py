#The notfier which sends to pushbullet
def PushbulletNotifier(**kwargs):
    print "PushbulletNotifier sending data %s " % (kwargs.get("weatherData"))