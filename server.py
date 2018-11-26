import jsonrpyc

class MyTarget(object):
    def greet(self, name):
        return "Hello, world, for %s!" % name

    def add(self, op1, op2):
        return op1 + op2

def main():
    # This won't be displayed because the stdin/out is wired to the server
    # print("Starting JSON server...")
    jsonrpyc.RPC(MyTarget())

if __name__ == '__main__':
    main()
