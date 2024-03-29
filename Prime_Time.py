import time
# I have no idea how to explain what exactly is happening here
# I myself made this program after brainstorming a lot
print("""This is a program to find the number of prime numbers
between any numbers you want.
""")

print("Enter '0' as both limits to exit the program.")
print("")

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False

    # to not count negative numbers
    if n < 0:
        return False

    #Yo could improve this function replacing n with sqrt(n)
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def count_primes_b2n(low_limit, max_limit):
    count = 0
    for i in range(low_limit + 1, max_limit):
        if is_prime(i):
            count += 1
            print(i, end=", ")

    if count == 0:
        print("None")
        print()
    else:
        print()
        print("Count:", count)

while True:
    try:
        print("")
        low_limit = int(input("Enter the lower limit: "))
        max_limit = int(input("Enter the upper limit: "))

        if max_limit == 0 and low_limit == 0:
            print("Exiting Program...")
            time.sleep(2)
            break
        if low_limit > max_limit:
            print("Wrong Interval. (Lower Limit > Upper Limit)")
            continue

        count_primes_b2n(low_limit, max_limit)
    except ValueError:
        print("Enter a number only.")
print('\n' + "Thank You!")
time.sleep(2)
                    
                        
