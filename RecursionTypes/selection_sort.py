def selection_sort(arr):
    length = len(arr)

    # Iterate through the entire list
    for i in range(length):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted List:", my_list)
