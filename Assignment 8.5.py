filename = input("Enter file name: ")
fileholder = open(filename)
count = 0
for line in fileholder:
    nline = line.rstrip()
    if 'From' in nline and'From:' not in nline:
        lsplit = nline.split()
        print(lsplit[1])
    else:
        continue
    count += 1
print("There were", count, "lines in the file with From as the first word")
