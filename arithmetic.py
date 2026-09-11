weight=float(input('enter your weight in (kg or lbs):   '))
unit=input('enter your unit(kg or lbs):    ')
if unit=="kg":
    weight = weight*2.205
    print(f"the weight in lbs is {weight}")
elif unit=="lbs":
    weight=weight*0.405
    print(f"the weight in kg is {weight}")
else :
       print(f"{unit} is not valid")