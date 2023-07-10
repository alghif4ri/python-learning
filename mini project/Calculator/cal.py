import function

def main():
    print("Welcome to calculator App!")

    while True:
        print("/Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice : ")

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == "1":
                result = function.add(num1, num2)
                print(f"Result: {result}")
            elif choice == "2":
                result = function.subtract(num1, num2)
                print(f"Result: {result}")
            elif choice == "3":
                result = function.multiply(num1, num2)
                print(f"Result: {result}")
            elif choice == "4":
                try:
                    result = function.divide(num1, num2)
                    print(f"Result: {result:.2f}") # round off upto 2
                #menampilkan error jika value yang diinput salah
                except ValueError as e:
                    print(str(e))
        elif choice == "5":
            print("Bye Bye!")
            break
        else:
            print("Please choose a valid option from menu...")

if __name__=="__main__":
    main()
