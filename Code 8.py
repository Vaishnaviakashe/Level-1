#using startswith() for string 

country = ["Australia","Brazil","Chilie","India","Ireland","Austria","Angola","Africa"]

for c in country[:]:
    if c.startswith("A"):
        country.remove(c)
        
print(country)