import time
import hashlib
import socket
import init
import lib
import protocol

Initizaling = init.Init()
Initizaling.Start()
Protocol = protocol.Protocol()

ip = lib.getIp()
peer = lib.getOnlinePeer()

print('Online peer is ' + peer)

lib.initExit()
