#Number classification

n = int(input("Enter number: "))

n = int(input("Enter number: "))

if n == 0:
    print("Zero")
elif n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
