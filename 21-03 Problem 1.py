def sum_avg(marks):
    total = sum(marks)
    average = total/len(marks)
    return total,average

marks=[96,95,71,64,84]
total,average=sum_avg(marks)
print(f"Total Marks:{total}")
print(f"Average Marks:{average}")
