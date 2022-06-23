text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
numog = text[pos + 2:]
numfloat = float(numog)
print(numfloat)
