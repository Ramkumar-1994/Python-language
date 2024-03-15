year=int(input("Enter year:"))

if(year%4==0):
  if(year%100!=0 or year%400==0):
      print("leap Year")
  else:
    print("Not Leap Year")
else:
  print("Not leap year")


if(year%4==0) and (year%100!=0 or year%400==0):
      print("leap Year")
else:
  print("Not leap year")

