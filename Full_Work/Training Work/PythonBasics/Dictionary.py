a = {'x':100, 'y':200}
b = list(a.items())
print(b)

Dict = {'Tim':18, 'Charlie':12, 'Tiffany':22, 'Robert':25}
print(Dict['Tiffany'])

# Copy Dictionary
Boys = {'Tim':18, 'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
StudentX = Boys.copy()
StudentY = Girls.copy()
print(StudentX)
print(StudentY)
# update Dictionary
Dict.update({"Sarah":9})
print(Dict)
# Deleting a Dictionary
del Dict['Charlie']
print(Dict)
# items Method
print("Students Name: %s" % Dict.items())

