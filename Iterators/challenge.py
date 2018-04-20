my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)
for i in my_list:
    print(i)