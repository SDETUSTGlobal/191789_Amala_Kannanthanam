#len method
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print ("Length : %d" % len (Dict))
# variable space
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("variable Type: %s" %type (Dict))
#str method
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print ("printable string:%s" % str (Dict))
#merge dictionary with update
my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict2 = {"firstName" : "Nick", "lastName": "Price"}
my_dict1.update(my_dict2)
print(my_dict1)
#merge dictionary ** method - kwargs
my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict2 = {"firstName" : "Nick", "lastName": "Price"}
my_dict = {**my_dict1, **my_dict2}
print(my_dict)
#dictionary membership test
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("email" in my_dict)
print("location" in my_dict)
print("test" in my_dict)
#append dictionary
my_dict = {"Name":[],"Address":[],"Age":[]};
my_dict["Name"].append("Guru")
my_dict["Address"].append("Mumbai")
my_dict["Age"].append(30)
print(my_dict)
#accessing dictionary elements
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("username :", my_dict['username'])
print("email : ", my_dict["email"])
print("location : ", my_dict["location"])
#deleting dictionary
my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
del my_dict1['username']
print(my_dict1)
my_dict1.clear()
print(my_dict1)
del(my_dict1)
#print(my_dict1)
#deletion with pop() method
my_dict5 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict5.pop("username")
print(my_dict5)
#append elements in dictionary
my_dict7 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict7['name']='Nick'
print(my_dict7)
#update exisitng elements in dictionary
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict["username"] = "ABC"
print(my_dict)
#insert one dictionary into another
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Washington"}
my_dict1 = {"firstName" : "Nick", "lastName": "Price"}
my_dict["name"] = my_dict1
print(my_dict)