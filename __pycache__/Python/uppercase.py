def string_test(s):
    d={'upper_case':0,'lower_case':0}
    for i in s:
        if i.isupper():
            d['upper_case']+=1
        elif i.islower():
            d['lower_case']+=1
        else:
            pass
    print("upper case letters:",d['upper_case'])
    print("upper case letters:",d['lower_case'])   
string_test("I Am Vishnu")               