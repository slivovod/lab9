import random as rnd
def random_filler(array, count):
    for i in range(count):
        array.append(rnd.randint(0, 100))

def max_value(array):
    mx = array[0]
    for i in array:
        if(mx < i):
            mx = i
    return mx

arr = []
n = int(input("how many numbers are in the list?\n"))
#random_filler(arr, n)
for i in range(n):
    arr.append(int(input()))
print(arr, "\nmax value: ", max_value(arr))
