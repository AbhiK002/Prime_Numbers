import math


def info():
    print("""This is a program to find the number of prime numbers
    between any numbers you want.
    """)
    print("Enter 'exit' anytime to exit the program." + '\n')


def get_limits():
    while True:
        lower_limit = input("Lower limit: ").lower()
        if lower_limit.isdecimal():
            if int(lower_limit) >= 0:
                break
            else:
                print("Try again with a natural number\n")
        else:
            if lower_limit == "exit":
                quit()
            else:
                print("Natural numbers allowed only\n")
            
        
    while True:
        upper_limit = input("Upper limit: ").lower()
        if upper_limit.isdecimal():
            if int(upper_limit) > int(lower_limit):
                break
            else:
                print("Upper limit needs to be greater than lower limit\n")
        else:
            if upper_limit == "exit":
                quit()
            else:
                print("Natural numbers allowed only\n")

    return int(lower_limit), int(upper_limit)


def print_primes(l, u):
    prime_list = []
    if l % 2 == 0:
        for num in range(l+1, u+1, 2):
            prime = True
            for i in range(3, int(math.sqrt(num)), 2):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                prime_list.append(str(num))
    else:
        for num in range(l, u+1, 2):
            prime = True
            for i in range(3, int(math.sqrt(num)), 2):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                prime_list.append(str(num))

    if prime_list:
        output = ', '.join(prime_list)
        return output
    else:
        return "None"


info()
low, upp = get_limits()
print(f"Prime numbers between {low} and {upp}:\n" + print_primes(low, upp))
