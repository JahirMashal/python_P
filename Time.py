from datetime import datetime

def whatsTheTime():
    now = datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%p")
    
    if current_time == "AM":
        return f"Today is {current_day} and it's before noon"
    else:
        return f"Today is {current_day} and it's past noon"
        
print(whatsTheTime())

