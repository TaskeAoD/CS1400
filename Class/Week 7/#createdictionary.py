#createdictionary

roster = {'Fred': 44, 'Ella': 39, 'Owen': 40, 'Zoe': 41, 'George': 44}
print(roster)

for k in roster.keys():
    print(k, end=' ')
print()

for v in roster.values():
    print(v, end=' ')
print()

for k, v in roster.items():
    print(k, v)

