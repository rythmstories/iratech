# Question.

# Write a Python Code that takes input as the values of x, y, a, b to solve the following equation:
# [ {x + (1/y) }a * {x – (1/y)}b ] / [ {y + (1/x) }a * {y – (1/x)}b ]


# Solution

def for_add(m,n,k):
	to_return_val = (m+(1/n))**k
	return to_return_val

def for_subtract(m,n,k):
	to_return_val = (m-(1/n))**k
	return to_return_val

x, y, a, b = list(map(float, input("Enter values of x, y, a, b in order using space: ").split()))
numerator = for_add(x,y,a)*for_subtract(x,y,b)
denominator = for_add(y,x,a)*for_subtract(y,x,b)
answer = numerator/denominator
print("Solving the equation gives the answer: ", answer)
