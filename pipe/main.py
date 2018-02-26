import sys

# ref https://www.lifewithpython.com/2017/06/python-check-stdin-type.html

print("Receive args : {}".format(sys.argv))
if not sys.stdin.isatty():
    print("Receive stdin pipe :\n {}".format(sys.stdin.readlines()))
