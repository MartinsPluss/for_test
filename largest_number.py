my_list = [1235, 124, 155, 123, 15687, 589]
largest_num = 0

for number in my_list:
    if number > largest_num:
        largest_num = number

print(largest_num)

new_list = []
my_tuple = (15, 12, 13, 14, 1)
for tuple_number in my_tuple:
    new_list.append(tuple_number)

new_list.sort()
print(new_list[-1])

# adding third option to find largest number in list or tuple

print(max(my_tuple))
