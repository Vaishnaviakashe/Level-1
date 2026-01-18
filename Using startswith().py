#using startswith() for string 

country = ["Australia","Brazil","Chilie","India","Ireland","Austria","Angola","Africa"]

for c in country[:]:
    if c.startswith("A"):
        country.remove(c)
        
print(country)

#using startswith() for integer

numbers = [12, 25, 34, 19, 40]

for n in numbers[:]:                 # loop over a copy
    if str(n).startswith("1"):       # convert int → string
        numbers.remove(n)

print(numbers)

