km_day = int(input('Type in how many km you have covered on your first jogging practice.'))
no_less_km = int(input('Type in your training goal in km.'))
percent = int(input('Type in your expected progress from one training day to another in %'))
day = 1
print(f"Day #{day}: {km_day} km.")
while km_day < no_less_km:
    count_percent = (km_day / 100) * percent
    km_day = count_percent + km_day
    day += 1
    print(f"Day #{day}: {km_day:.2f} km.")

print(f"You will reach your training goal on Day #{day} after you start practicing.")

