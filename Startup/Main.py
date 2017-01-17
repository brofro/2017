#The main runnner class to be started by the master init.py
from Startup.Bootstrapper import Bootstrapper


'''

Sequence

1. Init Notifier classes from INotifier
    - Notifiers(subscribers) take data and send to a destination endpoint

1.5 TODO Init Handler classes
    - Handlers take raw data and process them (and send to notifier list if necessary)

2. Init Services w/ Notifier and Handlers

3. Start/Stop Services

'''

bootstrapper = Bootstrapper()
notifiers = bootstrapper.GetNotifiers()
services = bootstrapper.GetSerivces(notifiers)

bootstrapper.StartServices(services)
bootstrapper.StopServices(services)