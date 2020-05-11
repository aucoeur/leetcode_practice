def find(search_list, value):
    search_list.sort()

    start = 0
    end = len(search_list) - 1

    # Only running until both pointers reach each other (no overlapping)
    while start <= end:
        midpoint = (start + end) // 2

        if search_list[midpoint] == value:
            return midpoint
        elif search_list[midpoint] < value:
            # Set start at midpoint for next pass
            start = midpoint + 1
        elif search_list[midpoint] > value:
            # Set midpoint to be new end limit
            end = midpoint - 1
    raise ValueError('Item not found')
