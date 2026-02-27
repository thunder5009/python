age=int(input("Enter age: "))
if age>0 and age<=2:
    print("Infant")
elif age>2 and age <=18:
    print("Minor")
elif age>=19 and age <=50:
    print("Adult")
elif age>=51 and age<=70:
    print("Senior")
elif age>=71:
    print("Super Senior")
else:
    print("Age is Invalid")