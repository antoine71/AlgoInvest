"""This modules defines the function used to perform operation on lists"""


def sum_lists(list1, list2):
    """This function return a list calculated from the sum of each element of 2 lists"""
    return [x + y for x, y in zip(list1, list2)]


def product_lists(list1, list2):
    """This function return a list calculated from the product of each element of 2 lists"""
    return [x * y for x, y in zip(list1, list2)]
