# Question.

# Write a Python function to find the next number in the series:
# 2, 3, 10, 15, 26, 35, 50, 63, ?


# Solution

# function to create the series and run a loop till the requried position to find the value
def series(pos):
	series_list = [(position**2)+1 if position%2!=0 else (position**2)-1 for position in range(1,pos+1)]
	return series_list[pos-1]

# have taken position as 9 by default since that was what was asked in question, we can comment it in case we need to find at any other position by uncommenting the input statement
# pos = int(input("Enter the position where you want to find the number at in the series: "))
pos = 9
num_at_pos = series(pos)
print_msg = "Number at position {} is: {}".format(pos, num_at_pos)
print(print_msg)
