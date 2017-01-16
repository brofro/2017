#The handler which processes raw data and turns into Commute relevant data
def CommuteHandler(notifiers, **kwargs):
    if kwargs is None:
        print "CommuteHandler args error"
        return
    weather = kwargs.get('weatherData')
    print "CommuteHandler handling data " + weather

    for notifier in notifiers:
        notifier.Notify(**kwargs)