filename = input("Enter file name: ")
fileholder = open(filename)
count = 0
emails = {}
for line in fileholder:
    nline = line.rstrip()
    if 'From' in nline and not "From:" in nline:
        lsplit = nline.split()
        emails[lsplit[1]] = emails.get(lsplit[1], 0) + 1
    else:
        continue

bcount = None
bemail = None

for email,occurrences in emails.items():
    if bcount is None or occurrences > bcount:
        bemail = email
        bcount = occurrences

print(bemail, bcount)
