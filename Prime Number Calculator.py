
def prime_checker(number):
    count = 0
    for divider in range(2, number):
        ramainder = number % divider
        if ramainder == 0:
            count += 1
    
    if count > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
        
n = int(input("Check this number: "))
prime_checker(number=n)
input("Press enter to exit.")
