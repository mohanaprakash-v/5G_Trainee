def recurse(k):
    if k > 0:
        result = k + recurse(k-1) #recursive function
        print(result)
    else:
        result = 0
    return result

print("Result Sum of numbers is:")
recurse(6)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1) #recursive function
fact = factorial(5)
print(f"Factorial of 5 is: {fact}")

