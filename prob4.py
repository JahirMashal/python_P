def firstThreeLower(input):
    if len(input) < 3 :
        return input.upper()
    else:
        nstring = input[:3].lower() + input[3:].upper()
        return nstring
    
    
print(firstThreeLower('SujeetPillai'))
print(firstThreeLower('Suj'))
print(firstThreeLower('Su'))