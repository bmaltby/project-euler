file = open("names.txt")

namedata = file.read()
namelist = namedata.split(',')
namedict = { }
for name in namelist:
    name = name.strip('"')
    score = 0
    for c in name:
        score += ord(c) - ord('A') + 1
    namedict[name] = score


sorted_names = namedict.keys()
sorted_names.sort()

total_score = 0
for i, n in enumerate(sorted_names):
    total_score += (i + 1) * namedict[n]

print total_score
