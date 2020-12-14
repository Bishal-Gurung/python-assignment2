names = []

print("List ID:", id(names))
names.append("Jocker")
names.append("Danny")
names.append("Maddie")
print("List ID:", id(names))
names.sort()
print("First", names[0])
print("Second", names[1])