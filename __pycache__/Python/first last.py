number=[10,20,30,40,50,10]
def first_last(number):
    first=number[0]
    last=number[-1]
    if first==last:
        return True
    else:
        return False
print(first_last(number))    