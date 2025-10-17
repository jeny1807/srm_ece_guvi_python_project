#find the factorial of a number using a loop
a=int(input("enter a number:"))
fact=1
for i in range(1,a+1):
   fact=fact*i
print(f"the factorial of{a}is{fact}")