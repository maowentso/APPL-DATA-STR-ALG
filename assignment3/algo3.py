
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

def radix_sort(s: str) -> str:
    if len(s) <= 1:
        return s

    codes = [ord(c) for c in s]
    base = 256
    max_code = max(codes)

    exp = 1
    while max_code // exp > 0:
        buckets = [[] for _ in range(base)]
        for c in codes:
            buckets[(c // exp) % base].append(c)
        codes = [c for bucket in buckets for c in bucket]
        exp *= base

    return "".join(map(chr, codes))

start_time = time.perf_counter()

output = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],quicksort_str)

end_time = time.perf_counter()

  
execution_time = end_time - start_time
print(f"quicksort: {execution_time:.6f}")
      
##quick = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],quicksort_str)
##radix = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],radix_sort_str)

start_time = time.perf_counter()

output = group_anagrams(["bucket","rat","mango","tango","ogtan","tar"],radix_sort)

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

output = group_anagrams(strings,radix_sort)

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"countingsort: {execution_time:.6f}")