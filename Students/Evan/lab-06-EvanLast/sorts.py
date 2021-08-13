import random
import time


def selection_sort(list):
    # Count Comparisons
    comps = 0
    # look thru list and find smallest value
    for fill_slot in range(len(list)):
        position_of_min = fill_slot
        # next pass (n + 1)st pass
        for location in range(fill_slot + 1, len(list)):
            if list[location] < list[position_of_min]:
                position_of_min = location
            # increment count of comparisons
            comps += 1
        list[fill_slot], list[position_of_min] = list[position_of_min], list[fill_slot]
    return comps


# always maintains a sorted sublist in the lower positions of the list
def insertion_sort(list):
    # Count Comparisons
    comps = 0
    for index in range(1, len(list)):
        current_value = list[index]
        position_index = index - 1
        if current_value > list[position_index]:
            comps += 1
        while current_value < list[position_index] and (position_index >= 0):
            # shift operation
            list[position_index+1] = list[position_index]
            position_index -= 1
            comps += 1
        list[position_index+1] = current_value
    return comps


def quick_sort(items, lo, hi):
    comparisons = 0
    if lo >= hi:
        return comparisons
    mid = (lo + hi) // 2
    # need to find the median of the low high and mid
    pivot = items[mid] # change this line
    lt, gt, i = lo, hi, lo
    while i <= gt:
        if items[i] < pivot:
            temp = items[i]
            items[i] = items[lt]
            items[lt] = temp
            i += 1
            lt += 1
            comparisons += 1
        elif items[i] > pivot:
            temp = items[i]
            items[i] = items[gt]
            items[gt] = temp
            gt -= 1
            comparisons += 2
        else:
            i += 1
            comparisons += 2
    comparisons += quick_sort(items, lo, lt - 1)
    comparisons += quick_sort(items, gt + 1, hi)
    return comparisons



def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

