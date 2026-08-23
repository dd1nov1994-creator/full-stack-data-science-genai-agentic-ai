def bubble_sort(arr):
    """Sort array using bubble sort algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the bubble sort
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Sorted array:", sorted_numbers)
