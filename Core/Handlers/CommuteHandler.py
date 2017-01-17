#The handler which processes raw data and turns into Commute relevant
#TODO Turn into class with static method collection
from Core.Handlers.Abstract.IHandler import IHandler


class CommuteHandler(IHandler):
    @staticmethod
    def Handle(notifiers, **kwargs):
        if kwargs is None:
            print ("CommuteHandler.Handle found no args")

        weather = kwargs.get('weatherData')
        print ("Commutehandler handling data " + weather)
        for notifier in notifiers:
            notifier.Notify(**kwargs)

def CommuteHandler(notifiers, **kwargs):
    if kwargs is None:
        print ("CommuteHandler args error")
        return
    weather = kwargs.get('weatherData')
    print ("CommuteHandler handling data " + weather)

    for notifier in notifiers:
        notifier.Notify(**kwargs)