counter = 0                     # global variable

def local_example():
    counter = 100               # a NEW local variable
    print("Inside (local):", counter)

def global_example():
    global counter              # use the global one
    counter += 1

local_example()
print("Outside:", counter)      # still 0
global_example()
global_example()
print("After global_example x2:", counter)   # 2
