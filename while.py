print("average number calculate")
all_number = 0
single_list = 0
user_input = input("put number into here use q to stop:")
while user_input != "q":
    num = float(user_input)
    all_number += num
    single_list += 1
    user_input = input("put number into here use q to stop")
if single_list == 0:
    result = 0
else:
    result = all_number / single_list
print("Your final number is：" + str(result))
