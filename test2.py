my_array = [64, 34, 25, 5, 22, 11, 90, 12]

print(my_array)
n = len(my_array)

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] < my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(my_array)