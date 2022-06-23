# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
nums = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")
        num = line[pos + 1:]
        num = num.strip()
        nums.append(num)
        count += 1
length = len(nums)
total = 0
for val in nums:
    total += float(val)
avg = float(total / length)
print("Average spam confidence: " + str(avg))
