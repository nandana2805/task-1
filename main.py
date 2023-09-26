def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Type of Error: Division by Zero"
    
print("select operator type:")
print("1:add")
print("2:substract")
print("3:multiply")
print("4:divide")

while True:
    choice = input("enter your choice:")

    if choice in ('1','2','3','4'):
        num1 = float(input("enter the first number:"))
        num2 = float(input("enter the second number:"))

        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",substract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
    else:
        print("invalid input")
    
    again = input("Do you want to perform calculation again? (yes/no): ")
    if again.lower() != 'yes':
        break

    