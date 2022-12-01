
groups = {}

with open("input.txt", "r") as f:
    data = f.readlines()

current = 1
for line in data:
    if (line == "\n") or (line == "\r\n") or line.isspace():
        current += 1
        continue
    
    print(f"{line.strip()}")
    if not (groups.get(f"group{current}")):
        groups[f"group{current}"] = int(line.strip())
    else:
        groups[f"group{current}"] += int(line.strip())

with open("output.txt", "a") as f:
    for k, v in groups.items():
        f.write(f"{k} - {v}\n")

total = 0

print()
for i in range(1, 4):
    tempn = 0
    tempg = ""
    for k, v in groups.items():
        if v > tempn:
            tempg = k
            tempn = v
    temp = groups.pop(tempg)
    total += temp
    print(f"{i} - {temp}")

print(f"\nTOTAL: {total}\n")
