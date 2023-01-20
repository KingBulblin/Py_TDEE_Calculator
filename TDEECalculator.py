import math
sex = input('Please enter your gender (M/F): ')
age = int(input('Please enter your age: '))
weight = float(input('Please enter your weight in pounds: '))
height = float(input('Please enter your height in inches: '))
weight = weight * 0.45359237
height = height * 2.54
if sex == 'm' or sex == 'M':
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
elif sex == 'f' or sex == 'F':
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
else:
    print('Sex could not be determined.')
    quit()
bmr = round(bmr)
print(f'Your Basal Metabolic Rate (BMR) is {bmr} calories a day. We will use your BMR to calculate your Total Daily Energy Expenditure (TDEE) based on exercise levels.')

activitylevel = int(input("What's your activity level? Please choose 1-5 (1 being lightly active, 5 being extra active): "))
if activitylevel == 1:
    activitylevel = 1.2
    workoutlevel = 'sedentary'
elif activitylevel == 2:
    activitylevel = 1.375
    workoutlevel = 'lightly active'
elif activitylevel == 3:
    activitylevel = 1.55
    workoutlevel = 'moderately active'
elif activitylevel == 4:
    activitylevel = 1.725
    workoutlevel = 'very active'
elif activitylevel == 5:
    activitylevel = 1.9
    workoutlevel = 'extremely active'
else:
    print('Activity level did not seem to have a valid response.')
    quit()
tdee = activitylevel * bmr

print(f"Based on the input you provided and that you are considered {workoutlevel}, you need {tdee} to maintain your current weight.")
print("It is important to know that the numbers provided to you are rough estimates of how many calories you need. Based on the Revised Harris-Benedict Equation which may provide close numbers but not exact.")