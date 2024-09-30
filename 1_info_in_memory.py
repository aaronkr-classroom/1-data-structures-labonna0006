# -*- coding: utf-8 -*-
"""1-info-in-memory.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ObpUIUflgxcgFMh32Mv1SNR4FkLYiJ66

# Array Value Swap

This is a simple problem where we are given an array of integers and we have to swap the values of the array at the given indices.

**Time Complexity:** The problem is simple and can be solved in O(1) time complexity.

![Array Swap](../img/1.1-array-swap.jpg)
"""

# Function to swap two values in an array
def swap(arr, index1, index2,):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp

# Example usage
array = [10, 20, 30, 40, 50]

print("Before swap:", array)

# Swap values at index 1 and index 3
swap(array, 1, 3)

print("After swap:", array)

"""# Insertion Sort

This is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

**Time Complexity:** The time complexity of the insertion sort is O(n^2) in the worst case.

![Insertion Sort](../img/1.2-insertion-sort.jpg)
"""

# Book solution
def insertion_sort(A, debug = 0):
  N = len(A)
  i = 1

  while i < N:
    current = A[i] # 11
    j = i - 1 # jth index = 0

    while j >=0 and A[j] > current:
      A[j + 1] = A[j] # 0th item saved into the 1st item
      j -= 1 # j = j-1

      if debug: # debug == 1 or debug == True
          print(f"Inside while: Array: {A}, current: {current}, i: {i}, j: {j}")

    A[j + 1] = current
    i += 1
    print(f"Array: {A}, current:{current}, i: {i}, j: {j}")


# Example usage
array = [12, 11, 13, 5, 6]
print("Original array:", array)
insertion_sort(array)
print("Sorted array:", array)

"""# String Equality

This is a simple problem where we are given two strings and we have to check if the strings are equal or not.

**Time Complexity:** The time complexity of the problem is O(n) where n is the length of the string.

![String Equality](../img/1.3-string-equality.jpg)
"""

# Function to check if two strings are exactly equal
def compare_strings_exactly(str1, str2):
  # same length
  if len(str1) != len(str2):
    print("str1 and str2 are NOT the same length!")
    return False


  # compare 1 by 1
  size = len(str1)
  i = 0 # string position index
  while i < size and str1[i] == str2[i]:
    i +=1

  print (f"Now at index: {i}")
  return i == size #if same, return True, if not same, return False


# Example usage
string1 = "hello"
string2 = "hello"

if compare_strings_exactly(string1, string2):
    print(f"{string1} and {string2} are exactly equal.")
else:
    print(f"{string1} and {string2} are not equal.")

