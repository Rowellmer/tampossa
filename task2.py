
# 
single_dimensional_array = ["apple", "banana", "cherry", "date"]

#
two_dimensional_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#
def display_single_dimensional_array(array):
    print("Elements in the single-dimensional array:")
    for element in array:
        print(element)

def display_two_dimensional_array(array):
    print("Elements in the two-dimensional array:")
    for sublist in array:
        print(sublist)
#
user_choice = input("Which array would you like to display? (single or two-dimensional): ").strip().lower()

if user_choice == "single":
    display_single_dimensional_array(single_dimensional_array)
elif user_choice == "two-dimensional":
    display_two_dimensional_array(two_dimensional_array)
else:
    print("Invalid choice. Please enter 'single' or 'two-dimensional'.")