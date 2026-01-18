#Check if year is leap or not

def is_leap(year):
    if year % 400 == 0:
        print("Leap")
        
    elif year % 100 == 0:
        print("Not Leap")
    elif year % 4 == 0:
        print("Leap")
        
    else:
        print("Not Leap")
        
year = int(input("Enter a year:"))
is_leap(year)