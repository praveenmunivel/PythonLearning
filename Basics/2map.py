
'''
map will take one function and argument(Iterable) and applies that function on top of that argument
The map function in Python applies a specified function to each item in an iterable (such as a list)
and returns a new iterable with the results
'''

def sqaure(a):
    return a*a
list_input = [1,2,3,4,5,6,7,8,9,10]
x = list(map(sqaure, list_input))
print(x)


y = list(map(lambda x : len(str(x)), list_input))
print(y)