from sorting_algo import bubble_sort
import pytest

def test_bubble_sort_works_with_small_list():
    test_list = [11, 4, 15, 2]
    result = [2,4,11,15]
    assert bubble_sort(test_list) == result


def test_bubble_sort_works_with_big_list():
    test_list = [
    42, 7, 119, 3, 88, 145, 61, 12, 97, 25,
    134, 56, 2, 78, 101, 49, 6, 140, 92, 31,
    115, 18, 73, 126, 44, 9, 137, 67, 23, 84,
    1, 109, 53, 14, 95, 38, 121, 71, 5, 132,
    27, 89, 148, 64, 16, 105, 47, 11, 82, 35,
    143, 58, 20, 99, 75, 4, 124, 69, 29, 111,
    51, 8, 136, 86, 33, 117, 62, 15, 94, 41,
    128, 72, 19, 107, 54, 10, 139, 80, 26, 113,
    46, 13, 91, 60, 22, 130, 77, 17, 103, 50,
    24, 142, 66, 30, 120, 57, 21, 98, 74, 36]
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
    23, 24, 25, 26, 27, 29, 30, 31, 33, 35, 36, 
    38, 41, 42, 44, 46, 47, 49, 50, 51, 53, 54, 
    56, 57, 58, 60, 61, 62, 64, 66, 67, 69, 71, 
    72, 73, 74, 75, 77, 78, 80, 82, 84, 86, 88, 
    89, 91, 92, 94, 95, 97, 98, 99, 101, 103, 
    105, 107, 109, 111, 113, 115, 117, 119, 
    120, 121, 124, 126, 128, 130, 132, 134, 
    136, 137, 139, 140, 142, 143, 145, 148]
    assert bubble_sort(test_list) == result

def test_bubble_sort_works_with_empty_list():
    test_list = []
    result = []
    assert bubble_sort(test_list) == result


def test_bubble_sort_dont_work_with_str():
    test_list = "string"
    result = "string"
    with pytest.raises(TypeError):
        bubble_sort(test_list) == result