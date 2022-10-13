"""Median calculator."""
def median(numbers):
    length = len(numbers)
    
    if length%2==0:
        
        #Lists index from 0 so I have to minus 1 
        median =((numbers[(int(length/2)-1)] + numbers[(int(length/2))])/2)
        
    else:#lists of an odd numbered size only have one number that could be the median
        
        median = numbers[int((length+1)/2)-1]
    return median
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
print(median(numbers))
