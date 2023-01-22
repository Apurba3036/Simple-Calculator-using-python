#sample-calculator

first=input("Enter fisrt value: ")
second=input("Enter second value: ")

f=float(first)
s=float(second)

print(".......press key for operator........")

op=input("Enter operator: ")

if op=="+":
    print (f+s)
elif op=="-":
    print(f-s)
elif op=="*":
    print(f*s)
elif op=="/":
    print(f/s)
elif op=="/":
    print(f/s)
elif op=="%":
    print(f%s)
    
else:
    print("Invalid operation")

