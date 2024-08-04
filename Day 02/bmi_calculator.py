# the codes below is for calculating BMI
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
# the two line of code above takes input from the user
#Write your code below this line 👇
# the height_square line performs the square of the height value and since its a float datatype
height_square = (float(height)) * (float(height))
# the line below takes the weight of the user in tnteger form 
actual_weight = int(weight)
# this line then perfoms the calculation of the BMI
bmi = int(actual_weight) / float(height_square)
print(int(bmi))