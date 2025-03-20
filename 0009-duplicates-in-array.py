# Given an array of integers, find all duplicates in the array.
def find_duplicates(arr):
    freq_dict = {}
    duplicates_list = []
    for element in arr:
        if element not in freq_dict:
            freq_dict[element] = 1
        else:
            duplicates_list.append(element)
    return duplicates_list


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))  # Output: [2, 3]
