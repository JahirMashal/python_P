def filterBySpeed(input, speed):
    
    filterlist = [item for item in input if item['speed'] == speed]
    return filterlist


print(filterBySpeed([{'speed': 'fast', 'name': 'Alice'}, {'speed': 'medium', 'name': 'Sam'}, {'speed': 'slow', 'name': 'Matt'}, {'speed': 'medium', 'name': 'Randy'}], 'medium'))

