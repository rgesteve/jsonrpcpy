import jsonrpyc

class MyTarget(object):
    def greet(self, name):
        return "Hello, world, for %s!" % name

def main():
    print("Starting JSON server...")
    jsonrpyc.RPC(MyTarget())

if __name__ == '__main__':
    main()
