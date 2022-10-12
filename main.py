inp_str = input("Enter the string with num: ")
res={'Letter':0,'Digits':0}
print("Original String : " + inp_str)
for c in inp_str:
    if c.isdigit():
        res['Digits'] += 1
    elif c.isalpha():
        res['Letter']+=1

print("Extracted numbers from the list : ", res)
