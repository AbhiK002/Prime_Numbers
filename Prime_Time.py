import time
print("""This is a program to find the number of prime numbers
between any numbers you want.
""")
print("Enter '0' as both limits to exit the program.")
print("")
while True:
    try:
        print("")
        low_limit = int(input("Enter the lower limit: "))
        max_limit = int(input("Enter the upper limit: "))
        output = ""
        if max_limit == 0 and low_limit == 0:
            print("Exiting Program...")
            time.sleep(2)
            break
        if low_limit > max_limit:
            print("Wrong Interval. (Lower Limit > Upper Limit)")
        for number in range(low_limit + 1,max_limit):
            if number != 1 and number != 0:
                div_count = 0
                for factor in range(number + 1):
                    if factor != 0:
                        if number % factor == 0:
                            div_count += 1
                if div_count == 2:
                    output += str(number) + ", "
        if output != "":
            print(output[:-2] + '.')
        elif output == "":
            print("None")
    except ValueError:
        print("Enter a number only.")
print("THANK YOU")
time.sleep(1)
print("Made by AbhiK02")
time.sleep(2)
                    
                        
