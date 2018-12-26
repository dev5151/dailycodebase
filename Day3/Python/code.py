string1 = input()
string2 = input()
count = 0
if len(string1)!=len(string2):
    print("Strings are not  of the same length")
else:    
    for i in range (len(string1)):
        if string1[i]!=string2[i]:
            count=count+1
    print(count)
    
