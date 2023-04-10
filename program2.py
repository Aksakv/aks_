arr=[11,3,0,78,1,3,66,234,74,4]
print("Enter a 10 digit array:")
for i in range(0,10):
    x=int(input())
    arr.append(x)
print(arr)
for i in range(0,10):
    if arr[i]==0:
        print("Invalid input.Enter only non zero numbers.")
print("Enter a 10 digit array:")
for i in range(0,10):
    x=int(input())
    arr.append(x)
print(arr)
while True:
    print(f"The current array is {arr}")
    # check if all elements in the array are zero
    if all(num == 0 for num in arr):
        print("All elements in the array are zero. Exiting the program.")
        break
    
    # ask the user if they want to replace the last non-zero element with 0
    user_input = input("Do you want to replace the last non-zero element with 0? (Y/N)")
    
    if user_input.upper() == "Y":
        # find the index of the last non-zero element in the array
        last_non_zero_index = len(arr) - 1
        while arr[last_non_zero_index] == 0:
            last_non_zero_index -= 1
        
        # replace the last non-zero element with 0
        arr[last_non_zero_index] = 0
    elif user_input.upper() == "N":
        # exit the program if the user inputs N
        print("Exiting the program.")
        break
    else:
        # handle invalid input
        print("Invalid input. Please enter Y or N")


    
