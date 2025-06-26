weight=int(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print("Your BMI is: ", bmi)

from datetime import datetime
with open("bmi_record.txt", "a") as file:
    file.write(f"{datetime.now()}: Your BMI is: {bmi}\n")

# Underweight (below 18.5), Healthy Weight (18.5 to 24.9), 
# Overweight (25 to 29.9), and Obesity (30 or higher)

if bmi<18.5:
    print("You are Underweight.")
elif 18.5<= bmi <24.9:
    print("You have a Healthy Weight.")
elif 25<= bmi < 29.9:
    print("You are Overweight.")
elif bmi >= 30:
    print("You are Obese.")
else:
    print("Error... Invalid BMI value.")