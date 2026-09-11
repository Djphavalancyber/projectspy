temperature = float(input("the temperature of the hall is: "))
unit = input("unit of the temperature is: ")
if unit=="C":
        temp = round((temperature*9/5)+32,1)
        print(f"the temperature in f° is {temp}")
elif unit=="F":
    temp=round((temperature-32)*(5/9))
    print(f"the temperature in C° is {temp}")
else:
    print(f"the unit {unit} is invalid")