weight=int(input("Enter your weight:"))

height=float(input("Enter your height:"))
import math
bmi=round(weight/(height*height),2)
print(bmi)

if(bmi<16):
  category="Underweight"

elif(bmi > 18.5 or bmi<24.9):
  category="Normal"

elif(bmi>25 or bmi<29):
  category="Overweight"

else:
  category="Obese"

print("Your BMI is",category)

