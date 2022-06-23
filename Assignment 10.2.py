name = input("Enter file:")
file = open(name)
counts = dict()

for line in file:
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours,0) + 1

for key, val in sorted(counts.items()):
    print (key, val)
