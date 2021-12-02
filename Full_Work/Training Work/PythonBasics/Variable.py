f = 101
e = 200
print(f)
print(e)
def somefunction():
    global f
    print(f)
    f = "I am learning Python"
somefunction()
print(f)
del e
