Weight = int(input("Enter Your Weight:"))
Unit = input("l(bs) or K(gs)")
if Unit.upper() == " L ":
    Conversion = Weight * 0.45
    print(f"Your Weight is {Conversion} Kgs ")
else:
    Conversion = Weight / 0.45
    print(f"Your Weight is {Conversion} lbs")
print("Have a Great Day!!")
