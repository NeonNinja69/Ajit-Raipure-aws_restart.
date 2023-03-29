my_list = []

num_elements = int(input("How many elements do you want in your list? "))

for i in range(num_elements):
    element = input("Enter element {} of {}: ".format(i+1, num_elements))

    my_list.append(element)

print("Your list is:", my_list)
