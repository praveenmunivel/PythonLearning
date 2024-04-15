
# Example 1
x = 1

'''
lambda is an anonymous function which will take positional argument and do some operations on top of that
'''
value = lambda x : x*2

print(value(x))

# Example 2 : Lets try a list

print(value([1,2,3]))

# Example 3 : Multiple positional arguments

func2 = lambda a,b,c : a*b*c

print(func2(1,2,3))

# Example 4 : Sorting a list of tuples based on the second element

data = [(1, 3), (4, 1), (2, 8)]
sorted_data = sorted(data, key = lambda x : x[1])
print(sorted_data)

'''
Lambda functions are particularly useful in situations where you need a short, 
throwaway function for a specific operation
'''