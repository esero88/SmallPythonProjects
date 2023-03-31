#BMI = mass / height * height
name = input("Enter your name: ")

weight = int(input("Enter your weight in kilograms: "))

height = float(input("Enter your weight in meters: "))

BMI = weight / (height * height)

print(BMI)

if BMI > 0:
    if (BMI < 18.5):
        print(name + ", you are Underweight")
    elif (BMI <= 24.9):
        print(name + ", you are Normal weight")
    elif (BMI < 29.9):
        print(name + ", you are Overweight")
    elif (BMI < 34.9):
        print(name + ", you are Obese")
    elif (BMI < 39.9):
        print(name + ", you are severely obese")
    else:
        print(name + ", you are morbidly obese")
else:
    print("Enter valid input")