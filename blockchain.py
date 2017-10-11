class Blockchain:

    def __init__(self):
        self.blocks = []

    def __add__(self, block):
        if len(self.blocks) > 0:
            block.prev = self.blocks[-1].hash
        block.seal()
        block.validate()
        self.blocks.append(block)

    def validate(self):
        for i, block in enumerate(self.blocks):
            try:
                block.validate()
            except:
                raise Exception('Invalid blockchain at block {}'.format(i))

    def __repr__(self):
        return 'Blockchain blocks: {}'.format(len(self.blocks))

