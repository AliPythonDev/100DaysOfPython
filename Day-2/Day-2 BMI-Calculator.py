height = input("Enter your Height in meters: ")
weight = input("Enter your Weight in Kilograms: ")
height_as_float = float(height)
weight_as_int = int(weight)
bmi = weight_as_int / height_as_float ** 2
#OR we can also write this formula bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)
