# O(1) - Constant Time
# No matter how big the input, function always does just one thing.


boxes = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def build_boxes(array):
    print(boxes[0]) # O(1)
    print(boxes[1]) # O(1)
    print(boxes[2]) # O(1)


build_boxes(boxes) # O(3) reduce to O(1)