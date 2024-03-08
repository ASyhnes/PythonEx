def find_largest(numbers):
    if not numbers:  
        return None 
    plusgrand = numbers[0]
    for nombre in numbers:
        if nombre > plusgrand:
            plusgrand = nombre
    return plusgrand

print(find_largest([7, 17, 13, 19, 5]))
