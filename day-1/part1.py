input = open('input.txt', 'r')
Lines = input.readlines()

sum = 0

for line in Lines:
    cal_value = 0
    for c in line:
        if c.isnumeric():
            cal_value += 10*int(c)
            break
    for c in reversed(line):
        if c.isnumeric():
            cal_value += int(c)
            break
    print(cal_value)
    sum += cal_value

print(sum)
