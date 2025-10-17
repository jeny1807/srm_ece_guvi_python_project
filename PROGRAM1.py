#input a single character and check if its an alphabet,digit,or special symbol

character=input("enter any value:")
if character.isalpha():
    print(" alphabet")
elif character.isdigit():
    print(" digit")
elif character.isalnum():
    print("invalid")
else:
    print("special character")
