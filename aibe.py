


a = ( 1,2,3, "labas")

ilgis = len(a)

print(ilgis)

aibe = {5,8,7,9,}

aibe.add(10)

aibe.add(9)

print(aibe)

if 3 in aibe:
    print("yra")

sarasas = {1,2,1,2,1,3,4,4,4,}

aibe2 = set(sarasas)

print(aibe2)
if 1 in sarasas:
    print("yra")
if 1 in aibe2:
    print("yra")

print(aibe | aibe2)

print(aibe.union(aibe2))
print(aibe & aibe2)

print(aibe - aibe2)




