#calculator using python

def add(num1,num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

def sub(num1,num2):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    return result

def mul(num1,num2):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    return(result)

def div(num1,num2):
    if num2 == 0:
        print("Division by zero is not allowed")
        return None
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
    return result

def perc(num):
    result = num / 100
    print(f"{num}% = {result}")
    return result

cal_list = ["Addition","Subtraction","Multiplication","Division","Percentage"]
print("Operations you can perform:\n")

for i in range(len(cal_list)):
    print(i+1,".",cal_list[i])
    
def main():    
    while True:
        try:
            choice = int(input("Operation you want to perform (1-5): "))
            if choice not in range(1,6):
                print("Invalid choice! Please choice a number between 1 and 5")
                continue
        except ValueError:
            print("Invalid input!\n Please enter a number.")
            continue

        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter number 1 :"))
                num2 = float(input("Enter number 2 :"))
            except ValueError:
                print("Invalid input! Please enter a number")
                continue
        else:
            try:
                num = float(input("Enter number :"))
            except ValueError:
                print("Invalid input! Please enter a number")
                continue
    
        if choice == 1:
            add(num1,num2)

        elif choice == 2:
            sub(num1,num2)

        elif choice == 3:
            mul(num1,num2)

        elif choice == 4:
            div(num1,num2)
            
        elif choice == 5:
            perc(num)

        ch = input("Do you want another calculation {Y/N}:").strip().upper()
        if ch != 'Y':
            break
        
if __name__ == "__main__":
    main()

    
    
    
    
