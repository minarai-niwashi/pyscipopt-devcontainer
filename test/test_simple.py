from example.simple import main


def test_main():
    expected_x = 0.0
    expected_y = 0.0
    x, y = main()

    assert (
        x == expected_x and y == expected_y
    ), f"Expected (x,y)=({expected_x}, {expected_y}) but got (x,y)=({x}, {y})"
