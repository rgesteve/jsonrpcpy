import jsonrpyc
import sys, os
from subprocess import Popen, PIPE

print("Starting server")
p = Popen([sys.executable, "server.py"], stdin=PIPE, stdout=PIPE)
rpc = jsonrpyc.RPC(stdout=p.stdin, stdin=p.stdout)

print("Sending message")
print(rpc("greet", args=(), block=0.1))
print("Done!")

      
