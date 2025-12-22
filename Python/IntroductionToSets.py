def average(array):
    # your code goes here
    distinct_height = set(array)
    sum_of_arr = sum(distinct_height)
    avg = sum_of_arr / len(distinct_height)
    return avg
    # your code goes here

