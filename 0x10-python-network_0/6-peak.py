#!/usr/bin/python3
"""6-peak module
"""


def find_peak(list_of_integers):
    """find_peak: Function to find the peak of a list

    Args:
        list_of_integers (list): List to find a peak from it

    Returns:
        The peak number
    """
    if not list_of_integers:
        return None

    def binary_search_peak(nums, low, high):
        """binary search peak

        Args:
            nums (list): list of integers
            low (int): lowest number
            high (int): Highest number

        Returns:
            peak value: The peak  value
        """
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            return binary_search_peak(nums, mid + 1, high)
        else:
            return binary_search_peak(nums, low, mid)

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
