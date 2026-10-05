# converts total minutes into hour and remaining minutes


total_minutes=int(input("enter total minutes: " ))
hours = total_minutes//60
remaining_minutes = total_minutes%60
print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)