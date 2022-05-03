from reverse_polish_notation import resolve

def run():
    assert resolve("3,2,-,1,-,.")==0.0, "Should be 0.00"
    assert resolve("3,2,-,3,/,.")==0.3333333333333333, "Should be 0.33"
    assert resolve("4,3,/,2,1,*,-,.")==-0.6666666666666667, "Should be -0.67"
    assert resolve("4,3,-,2,1,#,/,.")==0.3333333333333333, "Should be 0.33"
    assert resolve("4,3,2,1,*,*,#,.")==10.0, "Should be 10.00"
    assert resolve("1,2,#,.")==3.0, "Should be 3.00"

if __name__ == "__main__":
    run()
    print("Everything passed")