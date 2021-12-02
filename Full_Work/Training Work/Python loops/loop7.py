#while loop#
#Example file for working with loops
x=0
#define a while loop
while(x <4):
		print(x)
		x = x+1

#
#Example file for working with loops
#
x=0
#define a while loop
#	while(x <4):
#		print x
#		x = x+1

#Define a for loop
for x in range(2,7):
		print(x)

#For Loop
#use a for loop over a collection
Months = ["Jan","Feb","Mar","April","May","June"]
for m in Months:
		print(m)

# How to use break statements in For Loop
# use a for loop over a collection
# Months = ["Jan","Feb","Mar","April","May","June"]
# for m in Months:
# print m

# use the break and continue statements
for x in range(10, 20):
    if (x == 15): break
    # if (x % 2 == 0) : continue
    print(x)

# How to use “continue statement” in For Loop
# use a for loop over a collection
# Months = ["Jan","Feb","Mar","April","May","June"]
# for m in Months:
# print m

# use the break and continue statements
for x in range(10, 20):
    # if (x == 15): break
    if (x % 5 == 0): continue
    print(x)

# Enumerate
# use a for loop over a collection
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months):
    print(i, m)

# use the break and continue statements

# for x in range (10,20):
# if (x == 15): break
# if (x % 5 == 0) : continue
# print x