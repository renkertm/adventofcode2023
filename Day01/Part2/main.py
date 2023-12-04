import re

file = open("../input.txt")

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0

for line in file.readlines():
    nums = []
    
    for n in [m.start() for m in re.finditer("(?=\d)", line)]:
        nums.append((n, int(line[n]))) 

    for n in numbers:
        #print([m.start() for m in re.finditer('(?=' + n + ')', line)])
        for i in [m.start() for m in re.finditer('(?=' + n + ')', line)]:
            nums.append((i, numbers.index(n) + 1))
            #print((i, numbers.index(n) + 1))
            pass
        pass

    nums = sorted(nums)

    sum += ((nums[0][1] * 10) + nums[len(nums)-1][1])
    pass

print(sum)
