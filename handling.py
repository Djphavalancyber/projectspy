try:
    num=(int(input("enter a number that divides by 100")))
    result=(100/num)
    print("Result:{}".format(result))
except ZeroDivisionError:
    print("enter a non zero number")
except ValueError:
    print("enter a valid number!")
finally:
    print("executed successfully")

