#Print unique character

data = input("Enter data:")
count = []

def count_unique(data):
    for d in data:
        if data.count(d) == 1:
            count.append(d)
        
    return count 

print(count_unique(data))