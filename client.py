import jsonrpyc
import sys, os
from subprocess import Popen, PIPE

print("Starting server")
p = Popen([sys.executable, "server.py"], stdin=PIPE, stdout=PIPE)
rpc = jsonrpyc.RPC(stdout=p.stdin, stdin=p.stdout)

def cb(err, res=None):
    if err:
        raise err
    print("Callback got: " + res)
    sys.exit(0)

print("Sending message")
print(rpc("greet", args=("John",), callback = cb))
print("Done!")

while True:
    pass
