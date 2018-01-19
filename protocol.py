import lib
import hashlib

class Protocol:
    def __init__(self):
        pass

    def getVersionFromMsg(self, msg):
        msg.split('#')
        return int(msg[0])

    def unpackMsg(self, ver, msg):
        if ver == 1:
            msg_raw = msg[len(str(ver) + '#'):].split('(')
            sender = msg_raw[0]
            msg_raw = msg.split(')')
            receiver = msg_raw[1]
            msg_raw = msg[2:]
            message = msg_raw[len(sender + '('):int('-' + str(len('(' + receiver)))]

            result = []
            if sender == '0.0.0.0':
                result.append('server')
            else:
                result.append(sender)

            if receiver == '0.0.0.0':
                result.append('server')
            elif receiver == '...':
                result.append('network')
            else:
                result.append(receiver)
            result.append(message)

            return result

    def readMsg(self, ver, msg):
        if ver == 1:
            print('It works!')
