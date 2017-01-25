import json

'''
The request model object for
Pushbullet Push/Note
'''
class PushNoteRequest(object):

    def __init__(self, title, body):
        self.properties = {}
        self.properties["type"] = "note"

        self.properties["title"] = title
        self.properties["body"] = body


    def ToJson(self):
        return json.dumps(self.properties).encode()
