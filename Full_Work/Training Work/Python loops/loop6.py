#For the above Switch case in Python

def SwitchExample(argument):
    switcher ={
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")
if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))
#Switch Case Statement in Python
#def function(argument):

    #switch(argument)
       # {
        #case 0:
           # return "This is Case Zero";
        #case 1:
            #return " This is Case One";
       # case 2:
            #return " This is Case Two ";
       # default:
           # return "nothing";
       # };
#};


