def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(10)
for i in num:
    print(i)

print("\n")
print("Calling the generator again: ", list(num))
