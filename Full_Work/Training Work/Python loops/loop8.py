#Codefor while loop
x = 0
while (x < 4):
    print(x)
    x = x + 1

#For Loop SimpleExample
x = 0
for x in range(2, 7):
    print(x)

#Useoffor loop in string
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for m in (Months):
    print(m)

#Usebreak-statement infor loop
    for x in range(10, 20):
        if (x == 15): break
        print(x)

#UseofContinuestatement infor loop
    for x in range(10, 20):
        if (x % 5 == 0): continue
        print(x)

#Codefor “enumerate function” with “ for loop”
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months):
    print(i, m)
