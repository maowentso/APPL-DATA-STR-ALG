
##Input: strings = ["bucket","rat","mango","tango","ogtan","tar"]

##Output: [["bucket"],["rat","tar"],["mango"],["tango","ogtan"]]
import random
import string
import time
from collections import defaultdict


def groupAnagram(List):
    ans = []
    seen = []
    for arr in List:
        sorted_word = "".join(sorted(arr))

        if sorted_word not in seen:
            seen.append(sorted_word)
            ans.append([arr])
        else:
            index = seen.index(sorted_word)
            ans[index].append(arr)
    return(ans)
print(groupAnagram(["bucket","rat","mango","tango","ogtan","tar"]))

def group_anagrams(strings, sort_algo):
    buckets = defaultdict(list)
    for w in strings:
        buckets[sort_algo(w)].append(w)
    return list(buckets.values())

def quicksort_str(s: str) -> str:
    chars = list(s)

    def quicksort(arr, low, high):
        if low < high:
            pivot_idx = partition(arr, low, high)
            quicksort(arr, low, pivot_idx - 1)
            quicksort(arr, pivot_idx + 1, high)

    def partition(arr, low, high):
        pivot = ord(arr[high])
        i = low - 1
        for j in range(low, high):
            if ord(arr[j]) <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(chars, 0, len(chars) - 1)
    return "".join(chars)

def counting_sort(s: str) -> str:
    if not s:
        return s
    
    count = [0] * 256
    for char in s:
        count[ord(char)] += 1
        
    sorted_chars = []
    for ascii_val in range(256):
        if count[ascii_val] > 0:
            sorted_chars.append(chr(ascii_val) * count[ascii_val])
            
    return "".join(sorted_chars)

start_time = time.perf_counter()

output = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],quicksort_str)

end_time = time.perf_counter()

  
execution_time = end_time - start_time
print(f"quicksort: {execution_time:.6f}")
      
##quick = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],quicksort_str)
##radix = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],radix_sort_str)

start_time = time.perf_counter()

output = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],counting_sort)

end_time = time.perf_counter()
  
execution_time = end_time - start_time
print(f"countingsort: {execution_time:.6f}")

strings = ["abcdefg" * 20 for _ in range(10000)]

start_time = time.perf_counter()

output = group_anagrams(strings,quicksort_str)

end_time = time.perf_counter()
 
execution_time = end_time - start_time
print(f"quicksort: {execution_time:.6f}")



start_time = time.perf_counter()

output = group_anagrams(strings,counting_sort)

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"countingsort: {execution_time:.6f}")