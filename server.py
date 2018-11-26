import jsonrpyc

class MyTarget(object):
    def greet(self):
        return "Hello, world!"

def main():
    print("Starting JSON server...")
    jsonrpyc.RPC(MyTarget())

if __name__ == '__main__':
    main()
