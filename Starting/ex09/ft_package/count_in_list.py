"""Count occurrences of an element in a list."""


def count_in_list(lst: list, item: any) -> int:
    """
    Count the number of occurrences of an item in a list.
    
    Args:
        lst: The list to search in.
        item: The item to count.
    
    Returns:
        The number of occurrences of item in lst.
    """
    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count
