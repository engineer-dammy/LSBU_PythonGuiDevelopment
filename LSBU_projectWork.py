file = open('3501343a.csv' , 'r')
firstline = True
heightTotal = 0
average = 0
heightCount = 0

for line in file:
    if firstline:
        firstline = False
    else:
        data = line.strip().split(',')
        data = [int(data[0])]
        for x in data:
            for y in range(33, 53 +1):
                if x == y:
                    heightTotal += x
print(heightTotal)






