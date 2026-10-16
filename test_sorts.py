import unittest
from merge_sort import merge_sort
from quick_sort import quick_sort

def test_empty_merge():
    assert merge_sort([]) == []

def test_single_merge():
    assert merge_sort([1]) == [1]

def test_ordered_merge():
    assert merge_sort([3,5,18,30,41]) == [3,5,18,30,41]

def test_simple_disordered_merge():
    assert merge_sort([3,1,4,5,2,8,6]) == [1,2,3,4,5,6,8]

def test_repeats_merge():
    assert merge_sort([3,4,3,2,1,3,5,6,4]) == [1,2,3,3,3,4,4,5,6]

def test_original_merge():
    numbers = [3,2,7,8,6,5]
    merge_sort(numbers)
    assert numbers == [3,2,7,8,6,5]


#TEST QUICK_SORT
def test_empty_quick():
    assert quick_sort([]) == []

def test_single_quick():
    assert quick_sort([1]) == [1]

def test_ordered_quick():
    assert quick_sort([3,5,18,30,41]) == [3,5,18,30,41]

def test_simple_disordered_quick():
    assert quick_sort([3,1,4,5,2,8,6]) == [1,2,3,4,5,6,8]

def test_repeats_quick():
    assert quick_sort([3,4,3,2,1,3,5,6,4]) == [1,2,3,3,3,4,4,5,6]

def test_original_quick():
    numbers = [3,2,7,8,6,5]
    quick_sort(numbers)
    assert numbers == [3,2,7,8,6,5]

    