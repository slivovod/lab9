def linear_search(sequince, element):
    for i in range(len(sequince)):
        if (sequince[i] == element):
            return i
    return -1


sequince = [-2, 0, 3, 5, 7, 8, 11, 18, 24, 2, 54, 1, 6, 10]
# element = 5

element = int(input("enter the element you are looking for: "))

print(linear_search(sequince, element))