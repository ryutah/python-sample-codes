import sys

print("Receive args : {}".format(sys.argv))
if not sys.stdin.isatty():
    print("Receive stdin pipe :\n {}".format(sys.stdin.readlines()))
