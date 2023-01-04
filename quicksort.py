import random

    # Python3 implementation of QuickSort


    # Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            i = i + 1


    # Swap the pivot element with
    # e greater element specified by i
    (array[i], array[high]) = (array[high], array[i])

    # Return the position from where partition is done
    print(array)
    return i

    # Function to perform quicksort


def quick_sort(array, first, last):
    if first < last:
        print("The Pivot is =", array[last])


        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, first, last)

        # Recursive call on the left of pivot
        quick_sort(array, first, pivot - 1)
        print(array[:pivot])
        # Recursive call on the right of pivot
        quick_sort(array, pivot + 1, last)
        print(array[pivot:])


    # Driver code

    # This code is contributed by Adnan Aliakbar

if __name__ == '__main__':
    print("Quick Sort")
    nEle = int(input('Sample Size: '))
    array = random.sample(range(10,99), nEle)
    print('Array elements:\n')
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print(f'Sorted array: {array}')

