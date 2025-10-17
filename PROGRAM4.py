#write a function to check the given string is palindrome or not
text=input("enter a string")
reversed_text=""
for i in text:
    reversed_text= i+ reversed_text
print("the palindrome of the given string is ",reversed_text)
if (text==reversed_text):
    print("palindrome")
else:
    print("not palindrome")
