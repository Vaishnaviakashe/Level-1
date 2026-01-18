#Age Checking 

age = int(input("Enter age: "))


if age < 0 or age > 120:
    print("Invalid !")
    
elif  age < 18:
    print("Child")
    
else :
    print("Adult")
