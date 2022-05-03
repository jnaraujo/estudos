from bubble_sort import sort


list1 = [34,6,3,12,4,7,5,2] # 7 elements
list1_o = [2,3,4,5,6,7,12,34] # 7 elements

list2 = [ x for x in range(999, -1, -1)] # 1000 elements
list2_o = [ x for x in range(1000)] # 1000 elements

def run():
    assert sort(list1) == list1_o, f"Should be {list1_o}"
    assert sort(list2) == list2_o, "Should be [0,1,2,3...998,999,1000]"

if __name__ == "__main__":
    run()
    print("Everything passed")