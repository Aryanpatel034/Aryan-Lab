def create_list(start,end):
    return[(x,x^2,x^3) for x in range(start,end+1)]

start,end=1,5
result=create_list(start,end)
print(result)
