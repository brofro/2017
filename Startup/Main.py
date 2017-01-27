from Startup.Bootstrapper import Bootstrapper


'''

Sequence

1. Init Notifier classes from INotifier
    - Notifiers(subscribers) take data and send to a destination endpoint

2. Init Handler classes
    - Handlers take raw data and process them (and send to notifier list if necessary)

3. Init Services w/ Notifier and Handlers

4. Start/Stop Services

'''

bootstrapper = Bootstrapper()
keyCollection = bootstrapper.LoadApiKeys()
notifiers = bootstrapper.GetNotifiers(keyCollection)
handlers = bootstrapper.GetHandlers()
services = bootstrapper.GetSerivces(handlers, notifiers, keyCollection)

bootstrapper.StartServices(services)
bootstrapper.StopServices(services)