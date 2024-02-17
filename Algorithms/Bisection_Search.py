
list_1 = [i for i in range(1, 1000)]

def bisect_search(sorted_list: list, element: int | float):
    def bisect_search_helper(sorted_list, element, low, high):
        pass


    if len(sorted_list) == 0:
        return False
    else:
        bisect_search_helper(sorted_list, element, 0, len(sorted_list) - 1)


def bisect_search2(sorted_list, element):
    def bisect_search_helper(L, element, low, high):
        if high == low:
            return L[low] == element
        
        mid = (low + high)//2

        if L[mid] == element:
            return True
        
        elif L[mid] > element:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, element, low, mid - 1)
            
        else:
            return bisect_search_helper(L, element, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, element, 0, len(L) - 1)
        