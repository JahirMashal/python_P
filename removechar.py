def removeCharAtPoint(input_string, position):
    if position < 0 or position >= len(input_string):
        return
    nstring = input_string[ : position ] + input_string[position + 1 : ]
    print(nstring)
    # new_string2 = input_string[position :-5 ] + input_string[-1 : position ]
    # print(new_string2)
    
print(removeCharAtPoint('SujeetPillai', 3))