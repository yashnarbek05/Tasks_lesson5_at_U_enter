
height = float(input("Enter height: "))
weight = float(input("Enter weight: "))
bmi = weight / height ** 2

print(f"Your bmi: {bmi:.5f}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi <+ 24.9:
    print("You are normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
else: print("You are obese")
