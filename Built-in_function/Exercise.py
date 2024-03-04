age=int(input("Enter your age:"))

years_left=60-age
days_left=365*years_left
month_left=years_left*12
week=years_left*52

print(f'years left: {years_left}\nDays left is {days_left}\nMonth left is: {month_left}\nWeek left is {week} ')