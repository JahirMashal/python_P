def addTwoElements(input, elem1, elem2):
    input.append(elem1)
    input.append(elem2)
    
    return input
    
print(addTwoElements([1, 2, 3], 4, 6))
print(addTwoElements([], 1, 1))