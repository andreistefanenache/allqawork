import statistics
with open('data') as file:
    text=file.readline()
grades=list(map(int,text.split(',')))
print(min(grades))
print(max(grades))
print(round(sum(grades)/len(grades),2))
print(statistics.mean(grades))
print(statistics.median(grades))
print("{} {} {} {} {}".format(min(grades),max(grades),round(sum(grades)/len(grades),2),statistics.mean(grades),statistics.median(grades)))
