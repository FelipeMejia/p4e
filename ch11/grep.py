import re

reg = input("Enter a regular expression: ")
fhand = open("mbox.txt")
count = 0

for line in fhand:
    line = line.rstrip()
    if re.search(reg, line):
        count += 1

print(f"mbox.txt had {count} lines that matched {reg}")
