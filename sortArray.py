def sortByElem(input, field):
    list = sorted(input, key=lambda x: x[field])
    return list
    
    
    

print(sortByElem([{'cost':1200, 'speed':100}, {'cost':1500, 'speed':300}, {'cost':2000, 'speed':175}], 'speed'))
print(sortByElem([{'weight':12, 'height':15}, {'weight':95, 'height':20}, {'weight':9, 'height':7}], 'weight'))