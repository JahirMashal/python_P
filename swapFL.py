def swapFirstLast(input):
    if len(input) < 2 :
        return 'error'
    
    input[0], input[-1] = input[-1], input[0]
    return input
    
    
print(swapFirstLast([1, 3, 9, 5]))
print(swapFirstLast([1]))
print(swapFirstLast([1, 3]))