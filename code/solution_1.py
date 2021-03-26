# Question.

# Create a Python Function to perform a calculation based on the following mathematical function

# i=n
#  ∑ 	1 / (x^i)
# i=1

# Do not use the Math library to perform this task. Perform this task using two different methods. One of
# the methods should be using recursion.


# Solution

# method 1 with recursion
def recursion_func(x,n, ans=0):
    if n == 1:
        return (ans + 1/(x**n))
    else:
        return recursion_func(x, n-1, (ans + 1/(x**n)))

print(recursion_func(5, 10))


# method 2
def recursion_func_new(x,n):
    return sum( 1/(x**i) for i in range(1,n+1) )

print(recursion_func_new(5, 10))

