
# Problem 1 : Given a list of int, find the indices of which two numbers sum up to target
lst = [1,2,3,4,5,6,7]
target = 7

result_list = []
num_dict  = {}

for index, num in enumerate(lst):
    remainder = target - num
    if remainder in num_dict:
        result_list.append((num_dict[remainder], index))
    num_dict[num] = index

for i in result_list:
    print(i)


# Problem 2 : replace all the characters except one given character in a string of list

lst = ["abc", "ball", "abs", "jelly", "temp"]
character = 'b'
tb_replaced = '*'
result_list = []
for ele in lst:
    new_ele = ''.join(character if character == i else tb_replaced for i in ele)
    result_list.append(new_ele)

for i in result_list:
    print(i)