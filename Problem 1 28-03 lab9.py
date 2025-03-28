def countlowerupper(s):
    ans={"lowercase":0,"uppercase":0}

    for char in s:
        if char.islower():
            ans["lowercase"]+=1
        elif char.isupper():
            ans["uppercase"]+=1
    return ans
text = "Hello World"
output = countlowerupper(text)
print("uppercase and lowercase counts:",output)
