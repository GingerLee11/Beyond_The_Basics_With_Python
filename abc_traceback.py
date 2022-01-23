# python3
# abc_traceback.py - Learning how to read the traceback.

def a():
    print('Start of a()')
    b() # Call b()

def b():
    print('Start of b()')
    c() # Call c()

def c():
    print('Start of b()')
    42 / 0

a() # Call a()