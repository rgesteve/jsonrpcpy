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

def cb2(err, res=None):
    if err:
        print("Got an error while getting answer from add")
        raise err
    print(f"From the server got {res}")

print("Sending message")
rpc("greet", args=("John",), callback = cb)
rpc("add",   args=(7,2,), callback = cb2)
print("Done!")

while True:
    pass
