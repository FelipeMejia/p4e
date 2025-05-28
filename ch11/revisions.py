import re

file_name = input("Enter file: ")

fhand = open(file_name)
revisions = list()

for line in fhand:
    line = line.rstrip()
    useful_lines = re.findall("^New Revision: ([0-9]*.[0-9]*)", line)
    if useful_lines:
        revisions.append(int(useful_lines[0]))

revisions_avg = sum(revisions) / len(revisions)
print(revisions_avg)
