def sum():
    n = int(input("Enter the value of n: "))
    if n <= 0:
        print("Please enter a natural number.");
    else:
        print("Sum of the first of", n, "natural numbers is:", (n * (n + 1)) // 2)
sum()