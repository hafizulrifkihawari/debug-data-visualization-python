import json
from random import randint

def visualize(arr):
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    # examples
                    # {"content": "1", "tag": "1"}
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ]
    }
    return json.dumps(formatted)


arr = []
for i in range(0, 15):
    arr.append(randint(0, 100))

visualized = visualize(arr)

# insertion sort visualize
def insertion_sort(arr):
    for target_idx in range(1, len(arr)):
        target_value = arr[target_idx]
        compare_idx = target_idx - 1

        while compare_idx >= 0 and arr[compare_idx] > target_value:
            arr[compare_idx + 1] = arr[compare_idx]
            visualized = visualize(arr)
            compare_idx -= 1

        arr[compare_idx + 1] = target_value
        visualized = visualize(arr)

insertion_sort(arr)

# bubble sort visualize
# def bubble_sort(arr):
#     # We go through the list as many times as there are elements
#     for i in range(len(arr)):
#         # We want the last pair of adjacent elements to be (n-2, n-1)
#         for j in range(len(arr) - 1):
#             if arr[j] > arr[j+1]:
#                 # Swap
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 visualized = visualize(arr)

# bubble_sort(arr)