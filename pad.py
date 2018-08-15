ex1='.txt'
ex2='.doc'
ex3='.rtf'
print("Select your appropriate option: \n")
print("1. .txt\n2. .doc\n3. .rtf \n")
d=int(input("Enter here: "))
if(d==1):
	file=input("Enter the filename: (F:\Projects\Python\pppp): ")
	loc=file+ex1
	f=open(loc,"w")
	data=input("Enter your data here: ")
	f.write(data)
	f.close()
elif(d==2):
	file=input("Enter the filename: (F:\Projects\Python\pppp): ")
	loc=file+ex2
	f=open(loc,"w")
	data=input("Enter your data here: ")
	f.write(data)
	f.close()
elif(d==3):
	file=input("Enter the filename: (F:\Projects\Python\pppp): ")
	loc=file+ex3
	f=open(loc,"w")
	data=input("Enter your data here: ")
	f.write(data)
	f.close()
else:
	print("Wrong input")





