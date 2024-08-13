import string

def getUniqueWordCounts():
    
    with open('sample.txt', 'r') as file:
        text = file.read()
        
    text = text.lower()
    
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    words = text.split()
    
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
            
        else:
            word_counts[word] = 1
            
    return word_counts

print(getUniqueWordCounts())