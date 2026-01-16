#Age Checking 

age = int(input("Enter age: "))


if age < 0 or age > 120:
    print("Invalid !")
    
elif age > 0 and age < 18:
    print("Child")
    
elif age >= 18 :
    print("Adult")