names = [("Karan", "Shrestha", 23), ("Dhiraj", "Bariyat", 25), ("Arun", "Gurung", None)]

average_age = 0
age_counts = 0
for (first, second, age) in names:
    if age is not None:
        average_age += age
        age_counts += 1

average_age /= age_counts

print("The average age is:", average_age)

for (first, second, age) in names:
    if age is None:
        print(first, second, "unknown")
    elif age >= average_age:
        print(first, second, "old")
    else:
        print(first, second, "young")