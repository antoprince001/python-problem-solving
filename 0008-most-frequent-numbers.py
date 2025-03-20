def get_most_frequent_words(arr):
    count_dict = {}
    max_char = arr[0]
    max_count = 1
    for element in arr:
        if element not in count_dict.keys():
            count_dict[element] = 1
        else:
            count_dict[element] = count_dict[element] + 1
        if count_dict[element] > max_count:
            max_count = count_dict[element]
            max_char = element
    print(count_dict)
    return max_char


arr = [1, 3, 2, 1, 2, 2, 3, 3, 3, 1]
most_frequent_words = get_most_frequent_words(arr)
print(most_frequent_words)
