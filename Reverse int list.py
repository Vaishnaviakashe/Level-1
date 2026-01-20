#reverse list of integer 

input_list = [1,2,3,4]

#Using slicing

with_slicing = input_list[::-1]
print(with_slicing)

#Wihtout slicing

def reverse_int(input_list):
    reverse = []
    
    for i in input_list:
        reverse = [i] + reverse
        
    return reverse

print(reverse_int(input_list))