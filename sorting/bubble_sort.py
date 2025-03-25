num = [5,2,3,8,10,11]
# Repeatdly swap adjacent elements if they are in wrong order
def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num
print(bubble_sort(num))