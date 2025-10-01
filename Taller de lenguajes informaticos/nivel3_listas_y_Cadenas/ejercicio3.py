list = [1, 44, 37, 23, 44, 100, 34, 69, 23, 78, 12]
new_list =[]

for number in list:
   if number not in new_list:
       new_list.append(number)
print(new_list)
       