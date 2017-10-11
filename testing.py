from message import Message
from block import Block
from blockchain import Blockchain

foo = Message('hello world')
bar = Message('sent from', 'harrison', 'jake')

block1 = Block(foo, bar)

block2 = Block()
block2.add_message(Message('testing blockchain'))

chain = Blockchain()
chain.__add__(block1)
chain.__add__(block2)

print chain
