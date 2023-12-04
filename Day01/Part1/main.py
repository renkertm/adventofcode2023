import re

file = open("../input.txt")

sum = 0

for line in file.readlines():
    matches = re.findall('\d', line)
    sum += int(matches[0] + matches[len(matches)-1])
    pass

print(sum)