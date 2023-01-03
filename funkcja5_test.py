from funkcja5 import funkcja5

file = open('funkcja5_test.txt').readlines()

i = 1
for line in file:
    line = line.strip()
    print(str(i) + ':  ' + line)
    print(funkcja5(line))
    i += 1
