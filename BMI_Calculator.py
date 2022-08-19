# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


float_height = float(height)
int_weight = int(weight)

BMI = (int_weight / (float_height * float_height))
int_BMI = int(BMI)
print(int_BMI)