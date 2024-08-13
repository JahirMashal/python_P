def mulofSevenOrThree(input):
    if input % 3 == 0 or input % 7== 0:
        return True
    else:
        return False
        

print(mulofSevenOrThree(5))
print(mulofSevenOrThree(14))
print(mulofSevenOrThree(9))