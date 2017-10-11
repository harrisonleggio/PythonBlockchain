import hashlib
import time

class Block:

    def __init__(self, *args):
        self.messages = []
        self.timestamp = None
        self.prev = None
        self.hash = None

        if args:
            for arg in args:
                self.add_message(arg)

    def __get__block__hash__(self):
        to_hash = str(self.prev) + str(self.timestamp) + self.messages[-1].hash
        return hashlib.sha256(to_hash).hexdigest()

    def add_message(self, message):
        if len(self.messages) > 0:
            message.link(self.messages[-1])
        message.seal()
        message.validate_chain()
        self.messages.append(message)

    def link(self, block):
        self.prev = block.hash

    def seal(self):
        self.timestamp = time.time()
        self.hash = self.__get__block__hash__()

    def validate(self):
        for i, msg in enumerate(self.messages):
            try:
                msg.validate_chain()
                if i > 0 and msg.prev_hash != self.messages[i - 1].hash:
                    raise Exception("Invalid block: Message #{} has invalid message link in block: {}".format(i, str(self)))
            except:
                raise Exception("Invalid block: Message #{} In block: {}".format(i, str(self))
                )

    def __repr__(self):
        return 'Blockhash: {} Previous Hash: {} Messages: {} Time: {}'.format(
            self.hash, self.prev, len(self.messages), self.timestamp
        )



