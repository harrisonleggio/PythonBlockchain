import hashlib
import time

class Message:

    def __init__(self, data, sender=None, receiver=None):
        self.hash = None
        self.prev = None
        self.timestamp = time.time()
        self.length = len(data.encode('utf-8'))
        self.sender = sender
        self.receiver = receiver
        self.data = data
        self.payload_hash = self.__get_payload_hash__()

    def __get_payload_hash__(self):
        to_hash = str(self.timestamp) + str(self.data) + str(self.sender) + str(self.receiver)
        return hashlib.sha256(to_hash).hexdigest()


    def __get__message__hash__(self):
        to_hash = str(self.prev) + str(self.payload_hash)
        return hashlib.sha256(to_hash).hexdigest()

    def link(self, message):
        self.prev = message.hash
        return self

    def seal(self):
        self.hash = self.__get__message__hash__()
        return self

    def validate_chain(self):
        if self.payload_hash != self.__get_payload_hash__():
            raise Exception("Invalid payload hash in: {}".format(str(self)))
        if self.hash != self.__get__message__hash__():
            raise Exception("Invalid message hash in: {}".format(str(self)))

    def __repr__(self):
        return "Message Hash: {} Previous Hash: {} Sender: {} Receiver: {} Data:{}".format(
            self.hash, self.prev, self.sender, self.receiver, self.data[:25]
        )

