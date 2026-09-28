s1 = {6,9,1,6,2,0,2}
s1.add(40)
print("s1 :", s1)

s2 = {2,4,0}
print("s2 :", s2)

print(s1.difference(s2))#s1 - s2 commen ele are removed from s1
print(s1.symmetric_difference(s2))#combined ele are removed from both s1 and s2 and common elements removed
print(s1.union(s2))#all ele are taken from s1 and s2
print(s1.intersection(s2))#only commen ele
