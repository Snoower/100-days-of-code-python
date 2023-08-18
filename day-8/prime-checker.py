def prime_checker(number):
  is_prime = True
  if number == 1 or number == 0:
    print(f"{number} is not a prime number.")
  else: 
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime: 
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
