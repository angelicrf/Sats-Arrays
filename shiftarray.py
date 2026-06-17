# Create 3 arrays of 7 elements each
array1 = [0, 1, 2, 3, 4, 5, 6]      # Example values - change as needed
array2 = [10, 11, 12, 13, 14, 15, 16]
array3 = [20, 21, 22, 23, 24, 25, 26]

def cyclic_shift_push(arr1, arr2, arr3, user_input):
    if user_input != 1:
        return []   #return out of the loop

    saved_values = []  #push first and last elements
# foreach
    for i in [arr1, arr2, arr3]:
        first = i[0]
        last = i[-1]
        
        temp = i[0]                #save the last index
        for i in range(6):         # foreach
            i[i] = i[i + 1]         #manipulate and reassign elements to be +1 to the right
        i[6] = temp                     #old last to the new first
        
        saved_values.append((first, last))

    return saved_values


print("Initial state:")
print("Array1:", array1)
print("Array2:", array2)
print("Array3:", array3)

while True:

    user_input = int(input("Enter 1 to perform +1 cyclic shift push: "))
    if user_input == 0:
        print("Stopping the program.")
        break
    saved = cyclic_shift_push(array1, array2, array3, user_input)

    if saved:
        print("\nAfter +1 cyclic shift push:")
        print("Array1:", array1)
        print("Array2:", array2)
        print("Array3:", array3)
        
        print("\nSaved (pre-shift) first and last values for manipulation:")
        print("Array1 → first:", saved[0][0], " | last:", saved[0][1])
        print("Array2 → first:", saved[1][0], " | last:", saved[1][1])
        print("Array3 → first:", saved[2][0], " | last:", saved[2][1])
        
        print("\nThe saved values are now available for you to manipulate or re-insert as needed.")
    else:
        print("\nNo shift was performed (user input was not 1).")
