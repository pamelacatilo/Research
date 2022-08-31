human_year=int(input("Enter Dog age in Human years: "))
if human_year<=2:
    dog_year = human_year * 10.5
else:
    dog_year = 21 + (human_year - 2) * 4

print("Age in dog years: ",dog_year)


