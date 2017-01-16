def CommuteHandler(notifiers, **kwargs):
    if kwargs is None:
        print "CommuteHandler args error"
        return
    weather = kwargs.get('weatherData')
    print "CommuteHandler found weather data " + weather

    for notifier in notifiers:
        notifier(**kwargs)