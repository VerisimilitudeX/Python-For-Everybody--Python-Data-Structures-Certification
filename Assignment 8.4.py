fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    nlist = line.split()
    for word in nlist:
        if word in lst:
            continue
        else:
            lst.append(word.rstrip())
lst.sort()
print(lst)
