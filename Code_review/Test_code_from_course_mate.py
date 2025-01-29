def find_min(numbers):
    #counter = 0
    if len(numbers) == 0:
        print("The list is empty.")
        return
    counter = numbers[0]
    for item in numbers:
        if item < counter:
            counter = item
    print(f"the smallest item is:{counter}")

find_min([10,3-4,-11,])
find_min([])
find_min([100])