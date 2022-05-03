from binary_search import find


list1 = [2,3,4,5,6,7,12,34] # 7 elements
list2 = [ x for x in range(1000)] # 1000 elements

def run():
    assert find(4, list1) == 2, "Should be 2"
    assert find(1000, list1) == -1, "Should be -1"
    assert find(34, list1) == 7, "Should be 7"
    assert find(1001, list2) == -1, "Should be -1"
    assert find(999, list2) == 999, "Should be 999"

if __name__ == "__main__":
    run()
    print("Everything passed")