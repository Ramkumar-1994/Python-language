print("-------------Welcome to our Pizza Hut----------")

print("Order Now")

pizza_size=input("Enter your Pizza size:\n1.Small Pizza\n2.Medium Pizza\n3.Large Pizza\nChoose the option 1 or 2 or 3:")

pepperoni=input("Do you want pepperoni Y or N:")

extra_Cheese=input("Do you want Extra Cheese Y or N:")

if(pizza_size=='1'):
  bill=100
  if(pepperoni=='Y'):
    bill=bill+30
    if(extra_Cheese=='Y'):
      bill=bill+20
elif(pizza_size=='2'):
  bill=200
  if(pepperoni=='Y'):
    bill=bill+50
    if(extra_Cheese=='Y'):
      bill=bill+20
elif(pizza_size=='3' ):
  bill=300
  if(pepperoni=='Y'):
    bill=bill+50
    if(extra_Cheese=='Y'):
      bill=bill+20
else:
  print("Enter Valid input")

print(f'Your Total Bill is {bill}')





