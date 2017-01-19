from Core.Handlers.Abstract.IHandler import IHandler


'''
The distinct handler which processes data and determines if Commute is affected
This handler will send Commute relevant information to the provided INotifiers
'''
class CommuteHandler(IHandler):

    @staticmethod
    def Handle(notifiers, **kwargs):
        if kwargs is None:
            print ("CommuteHandler.Handle found no args")

        weather = kwargs.get('weatherData')
        print ("Commutehandler handling data " +
               weather.name + " has " + weather.weather[0]['main'])
        for notifier in notifiers:
            notifier.Notify(**kwargs)