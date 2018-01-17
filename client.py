import time
import hashlib
import socket
import init
import lib

Initizaling = init.Init()
Initizaling.Start()

peer = lib.getOnlinePeer()

print(peer)

lib.initExit()
