from json import dumps, dump, JSONEncoder
import re

class Player(JSONEncoder):
    __score = 0;
    __playerID = None
    __currentKey = {}

    def __init__(self, playerID):
        self.__score = 0
        self.__playerID = playerID

    def __call__(self, o):
        return o.__dict__

    def updateScore(self):
        self.__score += 1

    def resetScore(self):
        self.__score = 0

    def getScore(self):
        return self.__score

    def playerKeyNote(self):
        return self.__currentKey

    def getCurrentKey(self):
        return self.__currentKey.keys()[0]

    def getCurrentKeyValue(self):
        key = self.__currentKey.keys()[0]
        return self.__currentKey[key]
    
    def isEmptyKey(self):
        return self.__currentKey is None

    def setCurrentKey(self, value):
        self.__currentKey = value
        # self.__currentKey = { key: value, shuffledKey: 'abc'}

    def matchKey(self, userKey):
        if self.isEmptyKey():
            return self.toJSON()
        
        value = self.getCurrentKeyValue()
        value = re.sub(r'\d+', '', value)
        if value == userKey.lower():
            self.updateScore()
        self.setCurrentKey(None)
        return self.toJSON()

    def __str__(self):
        encode = self.toJSON()
        return encode

    def toJSON(self):
        # return dumps(self, skipkeys=False, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return dumps(self, skipkeys=True, default=self.__call__, sort_keys=True, indent=4)

# Antoher way to use default param in json.dumps method PlayerEncode(self)
class PlayerEncode(JSONEncoder):

    def __call__(self, o):
        return o.__dict__
