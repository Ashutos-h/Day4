#Answer 4
age=int(input("Enter your age:"))
sex=input("Enter your sex(M/F):")
mart=input("Enter your Maritial Status (Y/N):")
if sex=='F':
	print("You can work only in urban areas")
elif sex=='M' and age>=20 and age<=40:
	print("You can work anywhere")
elif sex=='M' and age>=40 and age<=60:
	print("You can work only in urban areas")
else:
	print("ERROR")
